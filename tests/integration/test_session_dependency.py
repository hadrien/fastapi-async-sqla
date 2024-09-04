from pytest import fixture
from sqlalchemy import select, text


@fixture
def app(app):
    from fastapi_async_sqla import Session

    @app.get("/session-dependency")
    async def get_session(session: Session):
        res = await session.execute(select(text("'OK'")))
        return {"data": res.scalar()}

    return app


async def test_it(client):
    response = await client.get("/session-dependency")
    assert response.status_code == 200
    assert response.json() == {"data": "OK"}
