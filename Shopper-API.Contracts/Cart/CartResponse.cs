namespace ShopperAPI.Contracts.Cart;

    public record CartResponse(
        Guid Id,
        string CustomerId,
        string CartId,
        List<string> Shoe
    ); 
