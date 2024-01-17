import tornado.web

accountDatabase = {
    "alice": {
        "realname": "Alice Smith",
        "dateOfBirth": "Jan 1st",
        "email": "alice@example.com"
    },
    "bob": {
        "realname": "Bob Jones",
        "dateOfBirth": "Dec. 31st",
        "email": "bob@bob.xyz"
    },
    "carol": {
        "realname": "Carol Ling",
        "dateOfBirth": "Jul. 17th",
        "email": "carol@example.com"
    },
    "dave": {
        "realname": "Dave N. Port",
        "dateOfBirth": "Mar.14th",
        "email": "dave@dave.dave"
    }
}

class ProfileHandler(tornado.web.RequestHandler):
    def get(self):
        p = self.request.path       #ex: /profile/alice
        uname = p.split("/")[2]
        realname = accountDatabase[uname]["realname"]
        dob = accountDatabase[uname]["dateOfBirth"]
        email = accountDatabase[uname]["email"]

        self.render("profilepage.html",
                    realname = realname,
                    dob = dob,
                    email = email
                    )

