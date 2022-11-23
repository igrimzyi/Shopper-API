namespace ShopperAPI.Contracts.Cart;

    public record CreateCartRequest(
    
        string CustomerId,
        string CartId,
        List<string> Shoe

    );
