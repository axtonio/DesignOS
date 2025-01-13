from flask import Flask, jsonify


API = Flask(__name__)


@API.route("/status", methods=["GET"])
async def status():
    """Gist detail view.
    ---
    get:
      parameters:
        - in: path
          schema: SpaceParameter
      responses:
        200:
          content:
            application/json:
              schema: ResultResponse
    """

    return jsonify(ok=True, result=True)
