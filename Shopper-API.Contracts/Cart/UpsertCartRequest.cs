namespace ShopperAPI.Contracts.Cart;

    public record UpsertCartRequest(
    
        string CustomerId,
        string CartId,
        List<string> Shoe
    );
