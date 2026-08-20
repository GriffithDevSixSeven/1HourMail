from typing import Optional
from redis.asyncio import Redis, ConnectionPool
from core.config import redis_settings

class RedisManager:

    def __init__(self):
        self._pool: Optional[ConnectionPool] = None
        self.client: Optional[Redis] = None

    def init_pool(self) -> None:
        
        if self._pool is None:

            self._pool = ConnectionPool.from_url(
                str(redis_settings.REDIS_URL),
                decode_responses=True,
                max_connections=20 
            )
            self.client = Redis(connection_pool=self._pool)

    async def close_pool(self) -> None:
        if self._pool:
            await self._pool.disconnect()
            self._pool = None
            self.client = None

redis_manager = RedisManager()


async def get_redis() -> Redis:
    if redis_manager.client is None:
        raise RuntimeError("Redis connection pool is not initialized!")
    return redis_manager.client
