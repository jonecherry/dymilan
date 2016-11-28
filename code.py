import web  
  
urls = (  
    '/', 'index'  
)  
  
class index:  
    def GET(self):  
        return 'holle work...'  
      
if __name__ == "__main__":  
    app = web.application(urls, globals())  
    app.run()  
