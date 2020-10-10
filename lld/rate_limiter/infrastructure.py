class Limit:
    limit_json = """
    {
	"serviceLimits": [{
			"service": "OrderService",
			"globalLimits": {
				"GET": {
					"limit": 20,
					"granularity": "second"
				},
				"POST": {
					"limit": 20,
					"granularity": "minute"
				}
			},
			"apiLimits": [{
					"methods": {
						"GET": {
							"limit": 15,
							"granularity": "second"
						},
						"POST": {
							"limit": 20,
							"granularity": "minute"
						}
					},
					"api": "CreateOrder"
				},
				{
					"methods": {
						"GET": {
							"limit": 10,
							"granularity": "second"
						},
						"POST": {
							"limit": 10,
							"granularity": "second"
						}
					},
					"api": "GetOrderById"
				}
			]
		},
		{
			"service": "DeliveryService",
			"globalLimits": {
				"GET": {
					"limit": 10,
					"granularity": "second"
				},
				"POST": {
					"limit": 20,
					"granularity": "minute"
				}
			},
			"apiLimits": []
		}
	]
}
    """
