package grailsproject

// Not sure exactly how this will work with social media authentication, but it's in here for now
class UserAccount {

    String emailAddress
    String password

    static hasOne = [profile: Profile]

    static mapping = {
    }

    static constraints = {
    }
}
