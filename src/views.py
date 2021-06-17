from flask import escape, request, Response
from src import app, db
from src.models import Rules
import json
from src.utils import rule_validator, following_rules, send_message


@app.route('/temp', methods=['POST'])
def temp():
    r = request.get_json()
    if "id" not in r or "value" not in r or "unit" not in r:
        return Response(json.dumps({"err": "invalid request"}), status=400, content_type="application/json")

    _rules = Rules.query.filter_by(device_id=r["id"]).all()
    for ru in _rules:
        if not following_rules(ru.context, r["value"], r["unit"]):
            message = {
                'msg': f'sensor: {r["id"]} broke rule: {ru}'
            }
            # TODO: SEND NOTIFICATION and Build Message function
            # currently only prints message
            send_message(message)
            return Response(json.dumps(message), status=200, content_type="application/json")

    return Response(json.dumps(r), status=200, content_type="application/json")


@app.route('/rules', methods=['POST'])
def rules():
    r = request.get_json()
    if "sensor" not in r or "rule" not in r:
        return Response(json.dumps({"err": "invalid request"}), status=400, content_type="application/json")

    if not rule_validator(r["rule"]):
        return Response(json.dumps({"err": "invalid request"}), status=400, content_type="application/json")

    new_rule = Rules(context=r['rule'], device_id=r['sensor'])
    try:
        db.session.add(new_rule)
        db.session.commit()
        msg = {
            "msg": "added rule",
            "rule": new_rule.context,
            "sensor": new_rule.device_id,
            "rule_id": new_rule.id
        }
        return Response(json.dumps(msg), status=200, content_type="application/json")

    except :
        return Response(json.dumps({"err": "error"}), status=400, content_type="application/json")


@app.route('/rules/<int:id>', methods=['DELETE', 'PUT'])
def rule(**kwargs):
    r: Rules = Rules.query.filter_by(id=kwargs['id']).first()
    if r is None:
        return Response(json.dumps({"err": "error"}), status=400, content_type="application/json")

    if request.method == 'DELETE':
        msg = {
            "msg": "DELETE",
            "rule_id": f"{kwargs['id']}"
        }
        db.session.delete(r)
        db.session.commit()
        return Response(json.dumps(msg), status=200, content_type="application/json")

    if request.method == 'PUT':
        data = request.get_json()
        if not data or 'rule' not in data or not rule_validator(data["rule"]):
            return Response(json.dumps({"err": "error"}), status=400, content_type="application/json")

        r.context = data["rule"]
        db.session.commit()
        msg = {
            "msg": "added rule",
            "rule": r.context,
            "sensor": r.device_id,
            "rule_id": r.id
        }
        return Response(json.dumps(msg), status=200, content_type="application/json")

