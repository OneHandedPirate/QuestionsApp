import httpx


async def get_questions(question_num: int):
    """get the passed number of questions from API"""

    async with httpx.AsyncClient() as client:
        res = await client.get(f'https://jservice.io/api/random?count={question_num}')

        return res.json()
