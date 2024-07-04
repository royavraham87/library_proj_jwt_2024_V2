# # Route for admin to add a user
# @app.route('/add_user', methods=['POST'])
# @jwt_required
# def add_user():
#     if request.role == 'admin':
#         data = request.get_json()
#         hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
#         new_user = User(
#             username=data['username'],
#             password=hashed_password,
#             role=data['role'],
#             name=data.get('name', ''),  # Use get with a default value
#             city=data.get('city', ''),  # Use get with a default value
#             age=data.get('age', -1)     # Use get with a default value
#         )
#         db.session.add(new_user)
#         db.session.commit()
#         return jsonify(user_to_dict(new_user))
#     else:
#         return jsonify({"message": "Unauthorized"}), 403



# # Route for admin to delete a customer
# @app.route('/delete_customer/<int:id>', methods=['DELETE'])
# @jwt_required
# def delete_customer(id):
#     if request.role == 'admin':
#         user = User.query.get(id)
#         if user and user.role == 'customer':
#             db.session.delete(user)
#             db.session.commit()
#             return jsonify({"message": "Customer deleted successfully"})
#         return jsonify({"message": "Customer not found or unauthorized"}), 404
#     else:
#         return jsonify({"message": "Unauthorized"}), 403


# # Route for admin to delete a book
# @app.route('/delete_book/<int:id>', methods=['DELETE'])
# @jwt_required
# def delete_book(id):
#     if request.role == 'admin':
#         book = Book.query.get(id)
#         if book:
#             db.session.delete(book)
#             db.session.commit()
#             return jsonify(book_to_dict(book))
#         else:
#             return jsonify({"message": "Book not found"}), 404
#     else:
#         return jsonify({"message": "Unauthorized"}), 403


# # Route for admin to update a customer
# @app.route('/update_customer/<int:id>', methods=['PUT'])
# @jwt_required
# def update_customer(id):
#     if request.role == 'admin':
#         user = User.query.get(id)
#         if user:
#             data = request.get_json()
#             user.username = data.get('username', user.username)
#             if 'password' in data:
#                 user.password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
#             user.role = data.get('role', user.role)
#             user.name = data.get('name', user.name)
#             user.city = data.get('city', user.city)
#             user.age = data.get('age', user.age)
#             db.session.commit()
#             return jsonify(user_to_dict(user))
#         else:
#             return jsonify({"message": "User not found"}), 404
#     else:
#         return jsonify({"message": "Unauthorized"}), 403