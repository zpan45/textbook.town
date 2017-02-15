package grailsproject

class Profile {
    String displayName
    String contactMethod
    // Need an instance variable for profile photo

    static belongsTo = [account: UserAccount]

    static hasMany = [bids: Bid, textbooks: Textbook]

    static constraints = {
    }
}
