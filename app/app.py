from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

# ============================================================
# Données des étudiants
# ============================================================

students = [
    {
        "id": 1,
        "first_name": "Ali",
        "last_name": "Alaoui",
        "email": "ali@example.com",
        "age": 22
    },
    {
        "id": 2,
        "first_name": "Sara",
        "last_name": "Amrani",
        "email": "sara@example.com",
        "age": 21
    }
]


# ============================================================
# Page principale
# ============================================================

@app.route("/")
def home():
    return send_from_directory(".", "index.html")


# ============================================================
# CSS
# ============================================================

@app.route("/style.css")
def style():
    return send_from_directory(".", "style.css")


# ============================================================
# API Hello
# ============================================================

@app.route("/api/hello", methods=["GET"])
def hello():
    return jsonify({
        "message": "Hello CI/CD"
    }), 200


# ============================================================
# GET - Tous les étudiants
# ============================================================

@app.route("/api/students", methods=["GET"])
def get_students():

    return jsonify({
        "success": True,
        "count": len(students),
        "data": students
    }), 200


# ============================================================
# GET - Étudiant par ID
# ============================================================

@app.route("/api/students/<int:student_id>", methods=["GET"])
def get_student(student_id):

    student = next(
        (s for s in students if s["id"] == student_id),
        None
    )

    if student is None:
        return jsonify({
            "success": False,
            "message": "Étudiant introuvable"
        }), 404

    return jsonify({
        "success": True,
        "data": student
    }), 200


# ============================================================
# POST - Créer un étudiant
# ============================================================

@app.route("/api/students", methods=["POST"])
def create_student():

    data = request.get_json()

    if not data:
        return jsonify({
            "success": False,
            "message": "Données JSON obligatoires"
        }), 400

    required_fields = [
        "first_name",
        "last_name",
        "email",
        "age"
    ]

    for field in required_fields:

        if field not in data:
            return jsonify({
                "success": False,
                "message": f"Champ obligatoire manquant : {field}"
            }), 400

    new_student = {
        "id": len(students) + 1,
        "first_name": data["first_name"],
        "last_name": data["last_name"],
        "email": data["email"],
        "age": data["age"]
    }

    students.append(new_student)

    return jsonify({
        "success": True,
        "message": "Étudiant créé avec succès",
        "data": new_student
    }), 201


# ============================================================
# PUT - Modifier un étudiant
# ============================================================

@app.route("/api/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):

    student = next(
        (s for s in students if s["id"] == student_id),
        None
    )

    if student is None:
        return jsonify({
            "success": False,
            "message": "Étudiant introuvable"
        }), 404

    data = request.get_json()

    if not data:
        return jsonify({
            "success": False,
            "message": "Données JSON obligatoires"
        }), 400

    student["first_name"] = data.get(
        "first_name",
        student["first_name"]
    )

    student["last_name"] = data.get(
        "last_name",
        student["last_name"]
    )

    student["email"] = data.get(
        "email",
        student["email"]
    )

    student["age"] = data.get(
        "age",
        student["age"]
    )

    return jsonify({
        "success": True,
        "message": "Étudiant modifié avec succès",
        "data": student
    }), 200


# ============================================================
# DELETE - Supprimer un étudiant
# ============================================================

@app.route("/api/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):

    student = next(
        (s for s in students if s["id"] == student_id),
        None
    )

    if student is None:
        return jsonify({
            "success": False,
            "message": "Étudiant introuvable"
        }), 404

    students.remove(student)

    return jsonify({
        "success": True,
        "message": "Étudiant supprimé avec succès"
    }), 204


# ============================================================
# Lancement
# ============================================================

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )