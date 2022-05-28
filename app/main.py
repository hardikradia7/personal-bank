from fastapi import FastAPI
from app.routes import v1


def main():
    application = FastAPI(title="Personal Bank",
                          description="Personal Banking Application",
                          version="1.0.0")
    v1.include_routes(application)
    return application


app = main()
