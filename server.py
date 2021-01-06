from aiohttp import web
from data_handler import get_data
import os

async def handleGet(request):
    try:
    	request_type =  request.rel_url.query['type']
    except:
    	return web.Response(text="You must send the parameter type", status=406)

    try:
    	data = get_data(request_type)
    	if data == -1:
    		return web.Response(text="You sent an invalid type parameter. Valid types: feminino, masculino, acessorio, all", status=406)
    except:
    	return web.Response(text="Something went wrong. Please try later", status=500)

    return web.json_response(body=data)

async def handleWelcome(request):
	return web.Response(text="This is not a web page")

app = web.Application()
app.add_routes([web.get('/produto', handleGet),
				web.get('', handleWelcome)])

if __name__ == '__main__':
    web.run_app(app, port=os.environ.get('PORT'), host='0.0.0.0')