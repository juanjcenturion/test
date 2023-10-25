#Python Imports.
from datetime import datetime, timedelta

#Framework Imports.
from flask.views import MethodView
from flask import request, jsonify
from flask_jwt_extended import ( 
    jwt_required, 
    create_access_token, 
    get_jwt_identity, 
    get_jwt)
from werkzeug.security import( 
    generate_password_hash, 
    check_password_hash
)

#Own imports
from app import database as db, app
from app.models.models import (
    User,
    Category,
    Comment,
    Post,
)
from app.schemas.schemas import (
    UserSchema,
    ShowUsersBasicSchema,
    CategorySchema
)


class UsersAPI(MethodView):
    @jwt_required()
    def get(self, user_id = None):
        additional_info = get_jwt()
        #Paginado Usuarios
        page = request.args.get('page', 1, type=int) #Def Value = 1
        can = request.args.get('can', 20, type= int) #Def Value = 20
        users = db.session.query(User).paginate(
        page=page, per_page=can

        )
        #Show all results whit paginate.
        if additional_info['is_admin']:
            if user_id is None:
                results =  UserSchema().dump(users, many=True)
            #Only selected for ID.
            else: 
                user = User.query.get(user_id)
                results = UserSchema().dump(user)
            return jsonify(results)
        else:
            if user_id is None:
                results =  ShowUsersBasicSchema().dump(users, many=True)
            #Only selected for ID.
            else: 
                user = User.query.get(user_id)
                results = ShowUsersBasicSchema().dump(user)
            return jsonify(results)

    def post(self):
        #Create User based in UserSchema
        user_json = UserSchema().load(request.json)
        username = user_json.get('username')
        password_hash = user_json.get('password_hash')
        is_admin = user_json.get('is_admin')
        
        #Hashed password gerator 
        password_hash = generate_password_hash(password_hash, method='pbkdf2', salt_length=16)

        #New User Data
        new_user = User(username=username, password_hash = password_hash, is_admin = is_admin)
        
        #Add to DB new user.
        db.session.add(new_user)
        db.session.commit()
        
        #Confirmation of created user
        return jsonify({
            'Usuario nuevo creado': username 
        }),200

    def put(self, user_id):
        user = User.query.get(user_id)
        user_json = UserSchema().load(request.json)
        username  = user_json.get('username')
        password_hash = user_json.get('password')
        is_admin = user_json.get('is_admin')
        if username is None:  
            #If only change the password
            password_hash = generate_password_hash(password_hash, method='pbkdf2', salt_length=16)
            user.is_admin = is_admin
            user.password_hash = password_hash 
            db.session.commit()
            return jsonify(mensaje=f"Modificaste la contraseña de: {user.username}")
        elif password_hash is None: 
            #If only change the Username
            user.is_admin = is_admin
            user.username = username
            db.session.commit()
            return jsonify(mensaje=f"Modificaste nombre de usuario a: {user.username}")
        else: 
            # Modify everything
            user.username = username
            password_hash = generate_password_hash(password_hash, method='pbkdf2', salt_length=16)
            user.password_hash = password_hash
            user.is_admin = is_admin
            db.session.commit()
            return jsonify(mensaje=f"Modificaste nombre de usuario y contraseña de: {user.username}")
    
    def delete(self, user_id):
        user = User.query.get(user_id)
        db.session.delete(user)
        db.session.commit()
        return jsonify(mensaje=f"Borraste el Usuario {user_id}")


app.add_url_rule("/user", view_func=UsersAPI.as_view('user'))
app.add_url_rule("/user/<user_id>", 
                view_func=UsersAPI.as_view('user_for_id')
                )


class CategoriesAPI(MethodView):
    def get(self, category_id = None):
        if category_id is None:
            categories = Category.query.all()
            result = CategorySchema(exclude=('id',)).dump(categories, many=True)
        else:
            category = Category.query.get(category_id)
            result = CategorySchema(exclude=('id',)).dump(category)
        return jsonify(result)
    
    def post(self):
        category_json = CategorySchema().load(request.json)
        name = category_json.get('name')
        new_category = Category(name=name)
        db.session.add(new_category)
        db.session.commit()
        return jsonify(f"Nueva Categoria agregada: {CategorySchema(exclude=('id',)).dump(new_category)}"), 201
    
    def put(self, category_id):
        category = Category.query.get(category_id)
        category_json = CategorySchema().load(request.json)
        name = category_json.get("name")
        category.name = name
        db.session.commit()
        return jsonify(f"Nombre de categoria cambiado: {CategorySchema(exclude=('id',)).dump(category)}")
    
    def delete(self, category_id):
        category = Category.query.get(category_id)
        db.session.delete(category)
        db.session.commit()
        return jsonify(mensaje=f"Borraste el pais {category}")


app.add_url_rule("/category", view_func=CategoriesAPI.as_view('category'))
app.add_url_rule("/category/<category_id>", 
                view_func=CategoriesAPI.as_view('category_for_id')
                )


@app.route('/login')
def login():
    data = request.authorization
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    #Check(contrasenia guardada, contrasenia recibida)
    if user and check_password_hash(user.password_hash, password):
        access_token = create_access_token(
            identity=username,
            expires_delta= timedelta(days=10),
            additional_claims={
                "is_admin":user.is_admin,
            }
        )
        return jsonify({"ok": access_token})
    return jsonify(error="no se puede generar el token"), 400