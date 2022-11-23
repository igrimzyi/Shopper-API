namespace Shopper-API.Contracts.Cart

    public record CartResponse(
        Guid Id,
        string CustomerId,
        string CartId,
        List<string> ProductIds
    ); 
