package grailsproject

class Auction {
    int minimumBid          // minimum price seller is willing to sell for
    float salePrice         // actual sale price (can be updated as each bid comes in until deadline)
    boolean isCurrent       // whether or not the
    // Need an instance variable for closing date and time--not sure what format that will be in- groovy Date?

    static hasOne = [textbook: Textbook]

    static hasMany = [bids: Bid]

    static constraints = {
    }
}
