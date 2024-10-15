import pytest
import config as cfg
from solution import solution_task2, solution_task3, solution_task4


@pytest.fixture(scope="module")
def fix_task2_soln():
    """Fixture to test the solution of task2"""

    return solution_task2()


def test_task2_shape(fix_task2_soln):
    """Test shape of radius and velocity vectors in task2 solution"""

    r, u = fix_task2_soln
    assert r.shape == (cfg.N,), f"solution_task2: shape of radius vector must be {cfg.N}"
    assert u.shape == (cfg.N,), f"solution_task2: shape of velocity vector must be {cfg.N}"


def test_task2_boundary_conditions(fix_task2_soln):
    """Test velocity boundary conditions in task2 solution"""

    r, u = fix_task2_soln
    assert u[-1] == 0, "solution_task2: velocity at the wall must be zero"
    assert u[0] > 0, "solution_task2: velocity at the center must be greater than zero"
    assert max(u) == u[0], "solution_task2: maximum velocity must be at the center"


def test_task2_true_value(fix_task2_soln):
    """Test velocity at the center in task2 solution"""

    r, u = fix_task2_soln
    true_vel = -cfg.dpdz / (4 * cfg.mu) * (cfg.R**2)
    assert abs(u[0] - true_vel) < 0.01 * \
        true_vel, "solution_task2: true value must be within 1 percent of analytical answer"


@pytest.fixture(scope="module")
def fix_task3_soln():
    """Fixture to test the solution of task3"""
    return solution_task3()


def test_task3_shape(fix_task3_soln):
    """Test shape of radius and velocity vectors in task3 solution"""

    r, u = fix_task3_soln
    assert r.shape == (cfg.N,), f"solution_task3: shape of radius vector must be {cfg.N}"
    assert u.shape == (cfg.N,), f"solution_task3: shape of velocity vector must be {cfg.N}"


def test_task3_boundary_conditions(fix_task3_soln):
    """Test velocity boundary conditions in task3 solution"""

    r, u = fix_task3_soln
    assert u[-1] == 0, "solution_task3: velocity at the wall must be zero"
    assert u[0] > 0, "solution_task3: velocity at the center must be greater than zero"
    assert max(u) == u[0], "solution_task3: maximum velocity must be at the center"


def test_task3_true_value(fix_task3_soln):
    """Test velocity at the center in task3 solution"""

    r, u = fix_task3_soln
    true_vel = -cfg.dpdz / (4 * cfg.mu_0) * (cfg.R**2)
    assert abs(u[0] - true_vel) < 0.01 * \
        true_vel, "solution_task3: true value must be within 1 percent of analytical answer"


@pytest.fixture(scope="module")
def fix_task4_soln():
    """Fixture to test the solution of task4"""

    return solution_task4()


def test_task4_shape(fix_task4_soln):
    """Test shape of radius, axial, and velocity matrices in task4 solution"""

    r, z, u = fix_task4_soln
    assert u.shape == (cfg.N, cfg.N), f"solution_task4: shape of velocity matrix must be {cfg.N} x {cfg.N}"
    assert r.shape == (cfg.N,), f"solution_task4: shape of radius vector must be {cfg.N}"
    assert z.shape == (cfg.N,), f"solution_task4: shape of axial vector must be {cfg.N}"


def test_task4_boundary_conditions(fix_task4_soln):
    """Test velocity boundary conditions in task4 solution"""

    r, z, u = fix_task4_soln

    assert abs(u[0].mean() - cfg.u_z_0) < 0.01 * \
        cfg.u_z_0, "solution_task4: average velocity at z = 0 must be within 1 percent of u_z_0"

    assert abs(u[-1].mean() - cfg.u_z_L) < 0.01 * \
        cfg.u_z_L, "solution_task4: average velocity at z = L must be within 1 percent of u_z_L"
    print(f"u[:, -1].mean() = {u[:, -1].mean()}")
    assert abs(u[:, -1].mean()) < 0.5, "solution_task4: average velocity at r = R must be close to zero"


#THi is just a test commit
