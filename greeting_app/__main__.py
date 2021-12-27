from greeting_app.create_app import create_app
import os
app = create_app("greeting_app.config.DevelopmentConfig")
app.run(host='0.0.0.0', port=os.getenv("PORT", 5000))
