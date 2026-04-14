#!/usr/bin/env python3
"""
MOSE Schema Validator v4.6.0
Validates MOSE instances and vertical OSs against the canonical schema.

Usage:
    python validate_mose.py <file_to_validate.json>
    python validate_mose.py --instance mose_instance.json
    python validate_mose.py --vertical vertical_os_example.json
"""

import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple, Any
import re

class MOSEValidator:
    def __init__(self, schema_path: str = "mose_schema.json"):
        """Initialize validator with schema"""
        self.schema_path = Path(schema_path)
        self.schema = self._load_json(self.schema_path)
        self.errors = []
        self.warnings = []
        self.info = []
        
    def _load_json(self, path: Path) -> Dict:
        """Load and parse JSON file"""
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            self._error(f"File not found: {path}")
            sys.exit(1)
        except json.JSONDecodeError as e:
            self._error(f"Invalid JSON in {path}: {e}")
            sys.exit(1)
    
    def _error(self, msg: str):
        """Add error message"""
        self.errors.append(f"❌ ERROR: {msg}")
    
    def _warning(self, msg: str):
        """Add warning message"""
        self.warnings.append(f"⚠️  WARNING: {msg}")
    
    def _info(self, msg: str):
        """Add info message"""
        self.info.append(f"ℹ️  INFO: {msg}")
    
    def _success(self, msg: str):
        """Print success message"""
        print(f"✅ {msg}")
    
    def validate_ocid(self, ocid: str) -> bool:
        """Validate OCID format"""
        pattern = r'^[A-Z]+-[A-Z0-9]+-v\d+\.\d+\.\d+-[A-Z]+-\d{8}T\d{6}Z$'
        if not re.match(pattern, ocid):
            self._error(f"Invalid OCID format: {ocid}")
            self._info("Expected format: TYPE-PROJECT-vMAJOR.MINOR.PATCH-OWNER-YYYYMMDDTHHMMSSZ")
            return False
        return True
    
    def validate_semver(self, version: str) -> bool:
        """Validate semantic version"""
        pattern = r'^\d+\.\d+\.\d+$'
        if not re.match(pattern, version):
            self._error(f"Invalid semver: {version}")
            self._info("Expected format: MAJOR.MINOR.PATCH (e.g., 4.6.0)")
            return False
        return True
    
    def validate_decision_weight(self, weight: int) -> bool:
        """Validate decision weight"""
        if weight not in [1, 3, 5]:
            self._error(f"Invalid decision weight: {weight}")
            self._info("Decision weight must be 1 (Advisory), 3 (Domain Lead), or 5 (Final Authority)")
            return False
        return True
    
    def validate_gate_code(self, code: str) -> bool:
        """Validate gate code"""
        valid_codes = ['S1', 'B1', 'L1', 'E1', 'EV1']
        if code not in valid_codes:
            self._error(f"Invalid gate code: {code}")
            self._info(f"Valid gate codes: {', '.join(valid_codes)}")
            return False
        return True
    
    def check_required_fields(self, data: Dict, required: List[str], context: str = "") -> bool:
        """Check if all required fields are present"""
        missing = [field for field in required if field not in data]
        if missing:
            self._error(f"Missing required fields in {context}: {', '.join(missing)}")
            return False
        return True
    
    def validate_system_identity(self, data: Dict) -> bool:
        """Validate system_identity section"""
        if 'system_identity' not in data:
            self._error("Missing system_identity section")
            return False
        
        si = data['system_identity']
        required = ['name', 'full_name', 'role', 'version', 'capabilities']
        
        if not self.check_required_fields(si, required, "system_identity"):
            return False
        
        # Validate version
        if not self.validate_semver(si['version']):
            return False
        
        # Check capabilities count
        if len(si['capabilities']) < 5:
            self._warning("system_identity.capabilities should have at least 5 items")
        
        self._success("system_identity validated")
        return True
    
    def validate_core_principles(self, data: Dict) -> bool:
        """Validate core_principles section"""
        if 'core_principles' not in data:
            self._error("Missing core_principles section")
            return False
        
        cp = data['core_principles']
        required = [
            'governance_before_generation',
            'single_source_of_truth',
            'multi_operator_intelligence',
            'rights_native_integration',
            'proof_based_execution'
        ]
        
        if not self.check_required_fields(cp, required, "core_principles"):
            return False
        
        # Validate enforcement
        for principle, details in cp.items():
            if 'enforcement' in details and details['enforcement'] not in ['required', 'optional']:
                self._error(f"Invalid enforcement value in {principle}: {details['enforcement']}")
                return False
        
        self._success("core_principles validated")
        return True
    
    def validate_architecture(self, data: Dict) -> bool:
        """Validate architecture section"""
        if 'architecture' not in data:
            self._error("Missing architecture section")
            return False
        
        arch = data['architecture']
        if 'layers' not in arch:
            self._error("Missing architecture.layers")
            return False
        
        layers = arch['layers']
        if len(layers) < 6:
            self._error(f"architecture.layers must have at least 6 layers, found {len(layers)}")
            return False
        
        # Validate each layer
        for i, layer in enumerate(layers, 1):
            required = ['name', 'purpose', 'order']
            if not self.check_required_fields(layer, required, f"architecture.layers[{i}]"):
                return False
            
            if layer['order'] < 1 or layer['order'] > 6:
                self._error(f"Layer order must be 1-6, found {layer['order']} in {layer['name']}")
                return False
        
        self._success("architecture validated")
        return True
    
    def validate_decision_framework(self, data: Dict) -> bool:
        """Validate decision_framework section"""
        if 'decision_framework' not in data:
            self._error("Missing decision_framework section")
            return False
        
        df = data['decision_framework']
        required = ['decision_object_v46', 'decision_weights', 'two_key_protocol']
        
        if not self.check_required_fields(df, required, "decision_framework"):
            return False
        
        # Validate decision_object_v46
        if 'required_fields' in df['decision_object_v46']:
            if len(df['decision_object_v46']['required_fields']) < 11:
                self._warning("decision_object_v46 should have at least 11 required fields")
        
        # Validate decision_weights
        dw = df['decision_weights']
        for weight in ['1', '3', '5']:
            if weight not in dw:
                self._error(f"Missing decision weight definition: {weight}")
                return False
        
        # Validate two_key_protocol
        tkp = df['two_key_protocol']
        if 'triggers' not in tkp or len(tkp['triggers']) < 5:
            self._warning("two_key_protocol.triggers should have at least 5 items")
        
        self._success("decision_framework validated")
        return True
    
    def validate_gate_framework(self, data: Dict) -> bool:
        """Validate gate_framework section"""
        if 'gate_framework' not in data:
            self._error("Missing gate_framework section")
            return False
        
        gf = data['gate_framework']
        if 'gates' not in gf:
            self._error("Missing gate_framework.gates")
            return False
        
        gates = gf['gates']
        if len(gates) < 5:
            self._error(f"gate_framework.gates must have at least 5 gates, found {len(gates)}")
            return False
        
        if len(gates) > 5:
            self._info(f"Found {len(gates)} gates (5 core + {len(gates)-5} custom) - Vertical OS extension detected")
        
        expected_codes = ['S1', 'B1', 'L1', 'E1', 'EV1']
        found_codes = [gate['code'] for gate in gates if 'code' in gate]
        
        # Check that all core gates are present
        missing_core_gates = [code for code in expected_codes if code not in found_codes]
        if missing_core_gates:
            self._error(f"Missing required core gate codes: {missing_core_gates}")
            return False
        
        # Info about custom gates
        custom_gates = [code for code in found_codes if code not in expected_codes]
        if custom_gates:
            self._info(f"Custom gates detected: {custom_gates}")
        
        for gate in gates:
            required = ['name', 'code', 'validates']
            if not self.check_required_fields(gate, required, f"gate {gate.get('code', 'unknown')}"):
                return False
            
            if len(gate['validates']) < 4:
                self._warning(f"Gate {gate['code']} should validate at least 4 items")
        
        self._success("gate_framework validated")
        return True
    
    def validate_rights_layer(self, data: Dict) -> bool:
        """Validate rights_layer section"""
        if 'rights_layer' not in data:
            self._error("Missing rights_layer section")
            return False
        
        rl = data['rights_layer']
        required = ['ocid_schema', 'voice_likeness_protection', 'drift_detection']
        
        if not self.check_required_fields(rl, required, "rights_layer"):
            return False
        
        self._success("rights_layer validated")
        return True
    
    def validate_operator_mesh(self, data: Dict) -> bool:
        """Validate operator_mesh section"""
        if 'operator_mesh' not in data:
            self._error("Missing operator_mesh section")
            return False
        
        om = data['operator_mesh']
        required = ['total_roles', 'families', 'role_schema']
        
        if not self.check_required_fields(om, required, "operator_mesh"):
            return False
        
        if om['total_roles'] < 35:
            self._error(f"operator_mesh.total_roles must be at least 35, found {om['total_roles']}")
            return False
        
        if om['total_roles'] > 35:
            self._info(f"Extended operator mesh: {om['total_roles']} roles (35 core + {om['total_roles']-35} custom)")
        
        if len(om['families']) < 7:
            self._error(f"operator_mesh.families must have at least 7 families, found {len(om['families'])}")
            return False
        
        self._success("operator_mesh validated")
        return True
    
    def validate_all_sections(self, data: Dict) -> bool:
        """Run all validation checks"""
        print(f"\n{'='*60}")
        print(f"MOSE VALIDATOR v4.6.0")
        print(f"{'='*60}\n")
        
        validations = [
            self.validate_system_identity,
            self.validate_core_principles,
            self.validate_architecture,
            self.validate_decision_framework,
            self.validate_gate_framework,
            self.validate_rights_layer,
            self.validate_operator_mesh,
        ]
        
        for validation_func in validations:
            if not validation_func(data):
                return False
        
        # Check for other required top-level sections
        required_sections = [
            'context_ledger',
            'os_factory',
            'drift_engine',
            'validation_pack',
            'versioning',
            'exports'
        ]
        
        for section in required_sections:
            if section not in data:
                self._error(f"Missing required section: {section}")
                return False
            else:
                self._success(f"{section} present")
        
        return True
    
    def print_report(self, valid: bool):
        """Print validation report"""
        print(f"\n{'='*60}")
        print("VALIDATION REPORT")
        print(f"{'='*60}\n")
        
        if self.info:
            print("📋 INFORMATION:")
            for msg in self.info:
                print(f"   {msg}")
            print()
        
        if self.warnings:
            print("⚠️  WARNINGS:")
            for msg in self.warnings:
                print(f"   {msg}")
            print()
        
        if self.errors:
            print("❌ ERRORS:")
            for msg in self.errors:
                print(f"   {msg}")
            print()
        
        print(f"{'='*60}")
        if valid and not self.errors:
            print("✅ VALIDATION PASSED")
            print(f"{'='*60}\n")
            return 0
        else:
            print("❌ VALIDATION FAILED")
            print(f"{'='*60}\n")
            return 1
    
    def validate_file(self, file_path: str) -> int:
        """Validate a MOSE instance file"""
        path = Path(file_path)
        
        if not path.exists():
            self._error(f"File not found: {file_path}")
            return self.print_report(False)
        
        print(f"Validating: {path.name}")
        data = self._load_json(path)
        
        valid = self.validate_all_sections(data)
        return self.print_report(valid)


def main():
    if len(sys.argv) < 2:
        print("Usage: python validate_mose.py <file_to_validate.json>")
        print("\nExamples:")
        print("  python validate_mose.py mose_instance.json")
        print("  python validate_mose.py vertical_os_example.json")
        sys.exit(1)
    
    file_to_validate = sys.argv[1]
    validator = MOSEValidator()
    exit_code = validator.validate_file(file_to_validate)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
