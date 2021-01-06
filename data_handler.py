from DatabaseUtils.DatabaseHandler import DatabaseHandler
import pandas as pd
import numpy as np
import json


def check_request_type(request_type):
	available_request_types = ['feminino', 'masculino', 'acessorio', 'all']
	if request_type not in available_request_types:
		return False
	return True

def get_data(request_type):

	if not check_request_type(request_type):
		return -1

	db = DatabaseHandler()
	
	query = "SELECT id_unico, produto, cores, tamanhos, valor, imagem_url FROM catalogo WHERE disponivel = CAST(1 AS BIT)"

	colNames = ['id_unico', 'produto', 'cores', 'tamanhos', 'valor', 'imagem_url']

	if (request_type != 'all'):
		query += " and tipo= '" + request_type + "'"

	data = db.query(query)

	rowCount = len(data)

	if (len(data) > 0):
		data = pd.DataFrame(np.array(data), columns= colNames)
		data = json.loads(data.to_json(orient="records") )
	data_treated = {"resultsCount": rowCount, "results": data}
	data_treated = json.dumps(data_treated)
	return data_treated
	

