from . import app


def activate(dp):
    dp.include_routers(
        
        app.router,
        
        )