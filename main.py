class RBAC:
    def __init__(self, role_perms): self.role_perms = role_perms
    def allowed(self, user_roles, perm):
        return any(perm in self.role_perms.get(r, set()) for r in user_roles)

if __name__ == "__main__":
    authz = RBAC({"viewer": {"repo:read"}, "admin": {"repo:read", "repo:delete"}})
    assert authz.allowed(["viewer"], "repo:read") and not authz.allowed(["viewer"], "repo:delete")
    print("[PASS] 073_rbac_policy_engine")
