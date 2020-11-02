from flask import Blueprint, jsonify, request, Response
from init.getdata import getmemoryindex
import logging

count = Blueprint("count", __name__)
popular = Blueprint("popular", __name__)

api_prefix = "/1/queries/"

@count.route(f"{api_prefix}/count/<requestprefix>")
def countA(requestprefix):
    logging.debug(f"prefix received {requestprefix}")
    distinctqueries = getqueriesfromprefix(requestprefix).drop_duplicates()
    return jsonify(count=len(distinctqueries.index))

@count.route(f"{api_prefix}/popular/<requestprefix>")
def popularA(requestprefix):
    topn = int(request.args.get("size"))
    result = getqueriesfromprefix(requestprefix).groupby(["Request"])["Request"].count().sort_values(ascending=False)[0:topn]
    print(result.to_json())
    return Response(result.to_json(), mimetype="application/json")

def gethigherbound(lowerbound):
    lastindex = len(lowerbound) - 1
    newlastchar = str(int(lowerbound[lastindex]) + 1)
    result = lowerbound[0:lastindex] + newlastchar
    logging.info(result)
    return result

def getqueriesfromprefix(prefix):
    indexed_data = getmemoryindex()
    return indexed_data.loc[(indexed_data.index >= prefix) & (indexed_data.index < gethigherbound(prefix))]
