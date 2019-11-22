from guillotina import configure


@configure.service(method="GET", name="@double/{value}")
async def double(context, request):
    return {"value": int(request.matchdict["value"]) * 2}
