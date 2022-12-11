from rest_access_policy import AccessPolicy


class AppBasicAccessPolicy(AccessPolicy):
    statements = [

        {
            "action": ["list"],
            "principal": ["*"],
            "effect": "allow",
            "condition": "is_superuser"

        },
        {
            "action": ["authentication"],
            "principal": ["*"],
            "effect": "allow",
            "condition": "is_superuser"
        }
    ]

    def is_superuser(self, request, view, action) -> bool:
        return request.user.is_superuser


class FormsPolicy(AccessPolicy):
    statements = [

        {
            "action": ["list"],
            "principal": ["*"],
            "effect": "allow",
            "condition": "is_superuser"

        },
        {
            "action": ["partial_update"],
            "principal": ["*"],
            "effect": "allow",
            "condition": "is_superuser"

        }
        ,{
            "action": ["get_form"],
            "principal": ["*"],
            "effect": "allow",

        },
    ]

    def is_superuser(self, request, view, action) -> bool:
        return request.user.is_superuser
