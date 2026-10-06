import os

from sqlalchemy import String, create_engine, select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column


class Base(DeclarativeBase):
    """Base class for SQLAlchemy ORM models."""
    pass


class User(Base):
    """SQLAlchemy ORM model representing a user."""

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False
    )
    email: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    def __repr__(self):
        return (
            f"User(id={self.id!r}, "
            f"username={self.username!r}, "
            f"email={self.email!r})"
        )


def get_engine():
    """Create and return the SQLAlchemy database engine."""
    database_url = os.getenv(
        "DATABASE_URL",
        "mysql+pymysql://root:yourpassword@localhost/example_db"
    )
    return create_engine(database_url, echo=False)


def create_tables(engine):
    """Create database tables defined by the ORM models."""
    Base.metadata.create_all(engine)


def create_user(session, username, email):
    """Create and persist a new User object."""
    if not username or not email:
        raise ValueError("Username and email are required.")

    user = User(username=username, email=email)
    session.add(user)

    try:
        session.commit()
        session.refresh(user)
        return user
    except SQLAlchemyError:
        session.rollback()
        raise


def get_user_by_username(session, username):
    """Retrieve a user by username."""
    statement = select(User).where(User.username == username)
    return session.scalars(statement).first()


def update_user_email(session, username, new_email):
    """Update the email address of an existing user."""
    user = get_user_by_username(session, username)

    if user is None:
        return None

    user.email = new_email

    try:
        session.commit()
        session.refresh(user)
        return user
    except SQLAlchemyError:
        session.rollback()
        raise


def delete_user(session, username):
    """Delete a user by username."""
    user = get_user_by_username(session, username)

    if user is None:
        return False

    try:
        session.delete(user)
        session.commit()
        return True
    except SQLAlchemyError:
        session.rollback()
        raise


def list_users(session):
    """Return all users."""
    statement = select(User).order_by(User.id)
    return list(session.scalars(statement).all())


def main():
    """Demonstrate SQLAlchemy ORM operations."""
    engine = get_engine()

    # Create the users table if it does not already exist.
    create_tables(engine)

    with Session(engine) as session:
        try:
            # Create a new user.
            user = create_user(
                session,
                "rejoice",
                "rejoice@example.com"
            )
            print("Created:", user)

            # Query for the user.
            found_user = get_user_by_username(session, "rejoice")
            print("Found:", found_user)

            # Update the user's email.
            updated_user = update_user_email(
                session,
                "rejoice",
                "new@example.com"
            )
            print("Updated:", updated_user)

            # List users.
            print("Users:")
            for current_user in list_users(session):
                print(current_user)

            # Delete the user.
            deleted = delete_user(session, "rejoice")
            print("Deleted:", deleted)

        except (SQLAlchemyError, ValueError) as error:
            print(f"Database operation failed: {error}")


if __name__ == "__main__":
    main()
