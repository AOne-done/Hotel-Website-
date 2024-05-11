from flask import Flask
# 1- Give Web Application Name
Web_App_Name  =Flask(__name__)
#Each Web application must has uniquee name to not happen any t3ared

# 2- Put all pathes of webpages(UI webpages) of my application home page login page services , ...

#2.0 main page domain osama.com not has thing after (osama.com)

@Web_App_Name.route("/")
#2.0.0 create method  that will back data that in this path
def homepagebackend():
    return "Hello From Flask Framework"


# 2.1 create next webpage  next name in my URL
@Web_App_Name.route("/about")
# 1- Give Web Application Name
Web_App_Name  =Flask(__name__)
#Each Web application must has uniquee name to not happen any t3ared

# 2- Put all pathes of webpages(UI webpages) of my application home page login page services , ...

#2.0 main page domain osama.com not has thing after (osama.com)

@Web_App_Name.route("/")
#2.0.0 create method  that will back data that in this path
def homepagebackend():
    return "Hello From Flask Framework"


# 2.1 create next webpage  next name in my URL
@Web_App_Name.route("/about")
def about():
    return "About Page From Flask"

# To Execute my Wep Application  (code mean just method execute if i run this file  not import it )
if __name__ == "__main__":
    Web_App_Name.run()


def about():
    return "About Page From Flask"



# To Execute my Wep Application  (code mean just method execute if i run this file  not import it )
if __name__ == "__main__":
    Web_App_Name.run()

