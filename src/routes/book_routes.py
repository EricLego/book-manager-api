@app.route('/api/books', methods=['GET'])
@require_auth
def get_books():
    return jsonify(books)
