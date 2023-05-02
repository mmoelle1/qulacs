from typing import List, overload

import qulacs_core

def drop_qubit(
    state: qulacs_core.QuantumState, target: List[int], projection: List[int]
) -> qulacs_core.QuantumState: ...
def from_json(json: str) -> qulacs_core.QuantumStateBase: ...
def inner_product(
    state_bra: qulacs_core.QuantumState, state_ket: qulacs_core.QuantumState
) -> complex: ...
def make_mixture(
    prob1: complex,
    state1: qulacs_core.QuantumStateBase,
    prob2: complex,
    state2: qulacs_core.QuantumStateBase,
) -> qulacs_core.DensityMatrix: ...
def make_superposition(
    coef1: complex,
    state1: qulacs_core.QuantumState,
    coef2: complex,
    state2: qulacs_core.QuantumState,
) -> qulacs_core.QuantumState: ...
@overload
def partial_trace(
    state: qulacs_core.QuantumState, target_traceout: List[int]
) -> qulacs_core.DensityMatrix: ...
@overload
def partial_trace(
    state: qulacs_core.DensityMatrix, target_traceout: List[int]
) -> qulacs_core.DensityMatrix: ...
@overload
def permutate_qubit(
    state: qulacs_core.QuantumState, qubit_order: List[int]
) -> qulacs_core.QuantumState: ...
@overload
def permutate_qubit(
    state: qulacs_core.DensityMatrix, qubit_order: List[int]
) -> qulacs_core.DensityMatrix: ...
@overload
def tensor_product(
    state_left: qulacs_core.QuantumState, state_right: qulacs_core.QuantumState
) -> qulacs_core.QuantumState: ...
@overload
def tensor_product(
    state_left: qulacs_core.DensityMatrix, state_right: qulacs_core.DensityMatrix
) -> qulacs_core.DensityMatrix: ...
