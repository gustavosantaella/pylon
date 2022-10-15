import json
from flask import jsonify
def response(*list,**dict:dict):
    additional = dict
    status = 200
    if 'status' in dict:
        status = dict['status'] 
        del dict['status']
        
    if 'data' in dict:
        data_str = convert_structure(dict['data'])     
        # data_str = type(dict["data"]) is str and jsonify(dict["data"]) or str(dict["data"])
        del dict['data']
        dict = {**data_str, **dict}
        
    else:
        dict = convert_structure(list)
        
        
    if type(dict) == tuple or type(dict) == list:
        dict = list
    else:
        if type(dict) == str:
            dict = dict
        else:
            dict = {**dict}
    
    for key in dict:
        if key in additional:
            del additional[key]
        
    return jsonify({
        "data":dict,
        "message":"Success",
        "status": status,
        **additional
    })
    
    
def convert_structure(data):
    try:
        if type(data) == tuple and len(data) == 1:
            loads = dict(json.loads(data[0])) 
            data_str = loads 
        elif type(data) == tuple:
            data_str = data
       
        else:
            data_str = json.loads(data)             
    except Exception as e:
            if type(data) == tuple:
                data_str = data[0]
            else:
                data_str = data
                
    
    
    return data_str