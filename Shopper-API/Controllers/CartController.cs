using Microsoft.AspNetCore.Mvc;
using ShopperAPI.Contracts.Cart;

namespace ShopperAPI.Controllers; 

[ApiController]

public class CartController : ControllerBase  
{
    [HttpPost("/cart")]
    public IActionResult CreateCart(CreateCartRequest request)
    {
        return Ok(request);
    }

    [HttpGet("/cart/{id:guid}")]
    public IActionResult GetCart(Guid id,UpsertCartRequest request)
    {
        return Ok(request);
    }

    [HttpDelete("/cart/{id:guid}")]
    public IActionResult DeleteCart(Guid id)
    {
        return Ok(id);
    }

}
