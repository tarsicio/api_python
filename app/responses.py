from flask import jsonify

def not_found():
	return jsonify(
		{
			'success': True,
			'data': {},
			'message': 'Resource not Found',
			'code': 404
		}), 404

def response(data):
	return jsonify({
		'success': True,
		'data': data
		}), 200