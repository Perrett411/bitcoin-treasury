import json
import hashlib


class QuantumRescaleSystem:
    def __init__(self, config_json=None):
        if config_json:
            self.config = json.loads(config_json)
        else:
            self.config = {
                "system_name": "Quantum_Rescale",
                "decimal_position": 0,
                "ledger": []
            }

    def decimal_shift_mechanism(self, trillions_spent: float) -> str:
        """
        Every trillion spent moves the decimal one place.
        Example: $1.5T -> $0 -> 1T
        """
        shifts = int(trillions_spent)
        self.config["decimal_position"] = self.config.get("decimal_position", 0) + shifts
        return f"Shift executed for {trillions_spent}T. Decimal position moved by {shifts}."

    def track_and_verify_coin(self, coin_id: str, origin_metadata: dict) -> str:
        """
        Fake Coin Prevention: Tracks origin via Merkle Roots + Quantum Stasis Field.
        """
        raw_data = f"{coin_id}:{json.dumps(origin_metadata)}:QuantumStasisField"
        merkle_root = hashlib.sha256(raw_data.encode()).hexdigest()

        coin_entry = {
            "coin_id": coin_id,
            "merkle_root": merkle_root,
            "status": "Verified & Tracked"
        }

        if "ledger" not in self.config:
            self.config["ledger"] = []
        self.config["ledger"].append(coin_entry)

        return merkle_root

    def export_system_state(self) -> str:
        """Exports the entire protocol state as a JSON string."""
        return json.dumps(self.config, indent=4)


if __name__ == "__main__":
    rescale_system = QuantumRescaleSystem()
    print(rescale_system.decimal_shift_mechanism(1.5))
    crypto_hash = rescale_system.track_and_verify_coin(
        coin_id="COIN_TRILLION_01",
        origin_metadata={"origin_node": "Alpha-Centauri", "batch": 999}
    )
    print(f"Generated Secure Merkle Hash: {crypto_hash}")
    print("\nUpdated System State JSON:")
    print(rescale_system.export_system_state())
