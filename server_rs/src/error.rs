use firestoredb;
use prost_twirp::ProstTwirpError;
use sqlitedb;
use std::{error::Error as StdError, fmt::Display};
use tonic;

#[derive(Debug)]
pub enum Error {
    Firestore(FirestoreError),
    SqliteDb(SqliteDbError),
    WeveEsi(ProstTwirpError),
}

impl From<Error> for tonic::Status {
    fn from(err: Error) -> Self {
        tonic::Status::internal(format!("{err}"))
    }
}

impl From<SqliteDbError> for Error {
    fn from(value: SqliteDbError) -> Self {
        Error::SqliteDb(value)
    }
}

impl From<FirestoreError> for Error {
    fn from(value: FirestoreError) -> Self {
        Error::Firestore(value)
    }
}

impl Display for Error {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        match self {
            Self::Firestore(e) => write!(f, "FirestoreError({})", e),
            Self::SqliteDb(e) => write!(f, "SqliteDbError({})", e),
            Self::WeveEsi(e) => write!(
                f,
                "WeveEsiError({})",
                match e {
                    ProstTwirpError::AfterBodyError {
                        body,
                        method,
                        version,
                        headers,
                        status,
                        err,
                    } => {
                        format!(
                        "Body: {}, Method: {:?}, Version: {:?}, Headers: {:?}, Status: {:?}, Error: {}",
                        match std::str::from_utf8(body) {
                            Ok(s) => s.to_string(),
                            Err(e) => e.to_string(),
                        },
                        method,
                        version,
                        headers,
                        status,
                        err,
                    )
                    }
                    other => format!("{}", other),
                }
            ),
        }
    }
}

impl StdError for Error {
    fn source(&self) -> Option<&(dyn StdError + 'static)> {
        match self {
            Error::Firestore(e) => Some(e),
            Error::SqliteDb(e) => Some(e),
            Error::WeveEsi(e) => Some(e),
        }
    }
}

#[derive(Debug)]
pub enum SqliteDbError {
    Initialize(sqlitedb::Error),
    NameMissing(u32),
    ReprocessMissing(u32),
    SelectName(sqlitedb::Error),
    SelectReprocess(sqlitedb::Error),
}

impl Display for SqliteDbError {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "{:?}", self)
    }
}

impl StdError for SqliteDbError {
    fn source(&self) -> Option<&(dyn StdError + 'static)> {
        match self {
            SqliteDbError::Initialize(e) => Some(e),
            SqliteDbError::NameMissing(_) => None,
            SqliteDbError::ReprocessMissing(_) => None,
            SqliteDbError::SelectName(e) => Some(e),
            SqliteDbError::SelectReprocess(e) => Some(e),
        }
    }
}

#[derive(Debug)]
pub enum FirestoreError {
    Initialize(firestoredb::Error),
    Read(firestoredb::Error),
    Write(firestoredb::Error),
}

impl Display for FirestoreError {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "{:?}", self)
    }
}

impl StdError for FirestoreError {
    fn source(&self) -> Option<&(dyn StdError + 'static)> {
        match self {
            FirestoreError::Initialize(e) => Some(e),
            FirestoreError::Read(e) => Some(e),
            FirestoreError::Write(e) => Some(e),
        }
    }
}
