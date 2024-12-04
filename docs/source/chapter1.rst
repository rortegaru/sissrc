Mathematical Foundation
=======================

Notation Rules and Algebra with Vectors and Tensors
----------------------------------------------------

In the mathematical formulation of quantities and fields, there are two types of notation which we shall use throughout the book: symbolic (or Gibbs') notation as well as index notation. For the sake of convenience and to provide suitably abstract formulations, we mostly prefer the symbolic notation. Let :math:`\boldsymbol{a}` and :math:`\boldsymbol{b}` be vectors in a (real) space of dimension :math:`D`.

.. math::

   \boldsymbol{a} = \begin{pmatrix}
   a_1 \\
   a_2 \\
   \vdots \\
   a_D
   \end{pmatrix} = a_i, \quad 
   \boldsymbol{b} = \begin{pmatrix}
   b_1 \\
   b_2 \\
   \vdots \\
   b_D
   \end{pmatrix} = b_i \quad (1 \leq i \leq D)

For the scalar (or dot) product:

.. math::

   \boldsymbol{a} \cdot \boldsymbol{b} = a_i b_i \quad (1 \leq i \leq D)

Using Einstein's summation convention:

.. math::

   a_i b_i = \sum_{i=1}^D a_i b_i,

where repeated indices are summed.

For the vector (or cross) product:

.. math::

   \boldsymbol{a} \times \boldsymbol{b} = \varepsilon_{ijk} a_i b_j \boldsymbol{e}_k = 
   \operatorname{det}\begin{pmatrix}
   a_1 & a_2 & \ldots & a_D \\
   b_1 & b_2 & \ldots & b_D \\
   \boldsymbol{e}_1 & \boldsymbol{e}_2 & \ldots & \boldsymbol{e}_D
   \end{pmatrix} \quad (1 \leq i, j, k \leq D),

where :math:`\varepsilon_{ijk}` is the permutation symbol (also known as the Levi-Civita tensor :math:`\varepsilon`), and :math:`e_i (1 \leq i \leq D)` are base vectors:

.. math::

   e_1 = \begin{pmatrix}
   1 \\
   0 \\
   \vdots \\
   0
   \end{pmatrix}, \quad 
   e_2 = \begin{pmatrix}
   0 \\
   1 \\
   \vdots \\
   0
   \end{pmatrix}, \quad 
   \ldots, \quad 
   e_D = \begin{pmatrix}
   0 \\
   0 \\
   \vdots \\
   1
   \end{pmatrix}.

The dot product of base vectors is given by:

.. math::

   e_i \cdot e_j = \delta = \delta_{ij},

where :math:`\delta` is the Kronecker symbol (unit or identity matrix):

.. math::

   \delta = \begin{pmatrix}
   1 & 0 & \cdots & 0 \\
   0 & 1 & \cdots & 0 \\
   \vdots & \vdots & \ddots & \vdots \\
   0 & 0 & \cdots & 1
   \end{pmatrix}, \quad 
   \delta_{ij} = \begin{cases}
   1 & \text{when } i = j, \\
   0 & \text{when } i \neq j.
   \end{cases}

For the dyadic (or tensor) product:

.. math::

   \boldsymbol{a} \otimes \boldsymbol{b} = a_i b_j = \begin{pmatrix}
   a_1 b_1 & a_1 b_2 & \cdots & a_1 b_D \\
   a_2 b_1 & a_2 b_2 & \cdots & a_2 b_D \\
   \vdots & \vdots & \ddots & \vdots \\
   a_D b_1 & a_D b_2 & \cdots & a_D b_D
   \end{pmatrix} \quad (1 \leq i, j \leq D).

This results in a second-order tensor :math:`A = a \otimes b`. Often, the multiplication symbol is omitted, and the tensor product is simply denoted as :math:`\boldsymbol{A} = \boldsymbol{ab}`.

The components :math:`a_1, a_2, \ldots, a_D` of :math:`\boldsymbol{a}` can also be expressed via summation:

.. math::

   \boldsymbol{a} = a_i \boldsymbol{e}_i \quad (1 \leq i \leq D).

The magnitude (or norm) of a vector :math:`\boldsymbol{a}` is given by:

.. math::

   \|\boldsymbol{a}\| = \sqrt{\boldsymbol{a} \cdot \boldsymbol{a}} = \sqrt{a_i a_i}.

If :math:`\|\boldsymbol{a}\| = 1`, the vector is called a unit vector, e.g., :math:`\boldsymbol{e}_i`. The normalized vector of :math:`\boldsymbol{a}` is:

.. math::

   \hat{\boldsymbol{a}} = \frac{\boldsymbol{a}}{\|\boldsymbol{a}\|} = \frac{a_i}{\sqrt{a_j a_j}} e_i.

It can be verified that :math:`\hat{\boldsymbol{a}}` is itself a unit vector since :math:`\|\hat{\boldsymbol{a}}\| = 1`.

Relations for Scalar and Vector Products
----------------------------------------

If :math:`\hat{\boldsymbol{a}}` and :math:`\hat{\boldsymbol{b}}` are unit vectors in the directions of :math:`\boldsymbol{a}` and :math:`\boldsymbol{b}`, respectively, then:

.. math::

   \hat{\boldsymbol{a}} \cdot \hat{\boldsymbol{b}} = \cos \theta,

where :math:`\theta` represents the angle between the two directions.

For vectors :math:`\boldsymbol{a}` and :math:`\boldsymbol{b}`:

.. math::

   \boldsymbol{a} = \|\boldsymbol{a}\| \hat{\boldsymbol{a}}, \quad 
   \boldsymbol{b} = \|\boldsymbol{b}\| \hat{\boldsymbol{b}}.

The scalar product becomes:

.. math::

   \boldsymbol{a} \cdot \boldsymbol{b} = \|\boldsymbol{a}\| \|\boldsymbol{b}\| \cos \theta.

**Projection of a Vector**

To project :math:`\boldsymbol{b}` onto the unit vector :math:`\hat{\boldsymbol{a}}`:

.. math::

   \|\boldsymbol{c}\| = \|\boldsymbol{b}\| \cos \theta = \hat{\boldsymbol{a}} \cdot \boldsymbol{b} = 
   \frac{\boldsymbol{a} \cdot \boldsymbol{b}}{\|\boldsymbol{a}\|}.

If the angle :math:`\theta` between the two vectors is a right angle (:math:`\theta = \pi/2`), then :math:`\cos \theta = 0`. Such vectors are orthogonal, and the condition for orthogonality is:

.. math::

   \boldsymbol{a} \cdot \boldsymbol{b} = 0.

**Cross Product**

The cross product :math:`\boldsymbol{a} \times \boldsymbol{b}` forms a vector normal to the plane defined by :math:`\boldsymbol{a}` and :math:`\boldsymbol{b}`:

.. math::

   \boldsymbol{a} \times \boldsymbol{b} = \|\boldsymbol{a}\| \|\boldsymbol{b}\| \sin \theta \hat{\boldsymbol{n}},

where :math:`\hat{\boldsymbol{n}}` is a unit vector normal to the plane of :math:`\boldsymbol{a}` and :math:`\boldsymbol{b}`. The magnitude :math:`\|\boldsymbol{a} \times \boldsymbol{b}\|` is the area of the parallelogram spanned by the vectors.

Coordinate System and Spatial Vector
------------------------------------

To describe physical objects in space and define their motion, we use the :math:`D`-dimensional Euclidean space :math:`\Re^D (D=1,2,3)`.

**Position Vector**

In an orthogonal Cartesian coordinate system:

.. math::

   \boldsymbol{x} = \begin{pmatrix}
   x_1 \\
   x_2 \\
   x_3
   \end{pmatrix} = \begin{pmatrix}
   x \\
   y \\
   z
   \end{pmatrix} \quad \text{in } \Re^3 (3D).

For :math:`\Re^2 (2D)`:

.. math::

   \boldsymbol{x}^T = \begin{pmatrix} x_1 & x_2 \end{pmatrix} = \begin{pmatrix} x & y \end{pmatrix}.

For :math:`\Re^1 (1D)`:

.. math::

   \boldsymbol{x}^T = \begin{pmatrix} x_1 \end{pmatrix} = \begin{pmatrix} x \end{pmatrix}.

**Gradient Operator in Cylindrical Coordinates**

The gradient operator is written as:

.. math::

   \nabla = \begin{pmatrix}
   \frac{\partial}{\partial r} \\
   \frac{1}{r} \frac{\partial}{\partial \phi} \\
   \frac{\partial}{\partial z}
   \end{pmatrix}.

If :math:`\boldsymbol{a}` is a vector in cylindrical coordinates :math:`\boldsymbol{a}^T = \begin{pmatrix} a_r & a_\phi & a_z \end{pmatrix}`, then the scalar product :math:`\nabla \cdot \boldsymbol{a}` becomes:

.. math::

   \nabla \cdot \boldsymbol{a} = \frac{1}{r} \frac{\partial (r a_r)}{\partial r} + \frac{1}{r} \frac{\partial a_\phi}{\partial \phi} + \frac{\partial a_z}{\partial z}.

**Curl in Cylindrical Coordinates**

The curl of :math:`\boldsymbol{a}` in cylindrical coordinates is:

.. math::

   \nabla \times \boldsymbol{a} = \begin{pmatrix}
   \frac{1}{r} \frac{\partial a_z}{\partial \phi} - \frac{\partial a_\phi}{\partial z} \\
   \frac{\partial a_r}{\partial z} - \frac{\partial a_z}{\partial r} \\
   \frac{1}{r} \left( \frac{\partial}{\partial r} (r a_\phi) - \frac{\partial a_r}{\partial \phi} \right)
   \end{pmatrix}.

Symmetric and Antisymmetric Tensors
-----------------------------------

A second-order tensor :math:`\boldsymbol{A} = A_{ij}` is symmetric if:

.. math::

   \boldsymbol{A} = \boldsymbol{A}^T \quad \text{or} \quad A_{ij} = A_{ji}.

Any tensor :math:`\boldsymbol{A}` can be written as the sum of symmetric and antisymmetric parts:

.. math::

   \boldsymbol{A} = \frac{1}{2} \left( \boldsymbol{A} + \boldsymbol{A}^T \right) + \frac{1}{2} \left( \boldsymbol{A} - \boldsymbol{A}^T \right),

where:

.. math::

   \boldsymbol{B}_s = \frac{1}{2} \left( \boldsymbol{A} + \boldsymbol{A}^T \right), \quad
   \boldsymbol{B}_a = \frac{1}{2} \left( \boldsymbol{A} - \boldsymbol{A}^T \right).

**Tensor and Vector Products**

The scalar product of a tensor :math:`\boldsymbol{A}` with a vector :math:`\boldsymbol{a}` is:

.. math::

   \boldsymbol{A} \cdot \boldsymbol{a} = \sum_i^D \boldsymbol{e}_i \sum_j^D A_{ij} a_j.

Conversely, the scalar product of a vector :math:`\boldsymbol{a}` with a tensor :math:`\boldsymbol{A}` is:

.. math::

   \boldsymbol{a} \cdot \boldsymbol{A} = \sum_i^D \boldsymbol{e}_i \sum_j^D a_j A_{ji}.

A tensor :math:`\boldsymbol{A}` is diagonal if all off-diagonal components are zero, i.e., :math:`A_{ij} = 0` for :math:`i \neq j`:

.. math::

   \boldsymbol{A} = \begin{pmatrix}
   A_{11} & 0 & \cdots & 0 \\
   0 & A_{22} & \cdots & 0 \\
   \vdots & \vdots & \ddots & \vdots \\
   0 & 0 & \cdots & A_{DD}
   \end{pmatrix}.

Diagonal tensors are always symmetric.

Scalar and Vector Projections
------------------------------

If :math:`\hat{\boldsymbol{a}}` and :math:`\hat{\boldsymbol{b}}` are unit vectors, then:

.. math::

   \hat{\boldsymbol{a}} \cdot \hat{\boldsymbol{b}} = \cos \theta,

where :math:`\theta` is the angle between the two directions. For vectors :math:`\boldsymbol{a}` and :math:`\boldsymbol{b}`, we find the scalar product:

.. math::

   \boldsymbol{a} \cdot \boldsymbol{b} = \|\boldsymbol{a}\| \|\boldsymbol{b}\| \cos \theta.

**Orthogonality**

Vectors are orthogonal if their scalar product is zero:

.. math::

   \boldsymbol{a} \cdot \boldsymbol{b} = 0 \quad \text{when } \theta = \frac{\pi}{2}.

**Cross Product**

The cross product :math:`\boldsymbol{a} \times \boldsymbol{b}` forms a vector normal to the plane of :math:`\boldsymbol{a}` and :math:`\boldsymbol{b}`:

.. math::

   \boldsymbol{a} \times \boldsymbol{b} = \|\boldsymbol{a}\| \|\boldsymbol{b}\| \sin \theta \hat{\boldsymbol{n}},

where :math:`\hat{\boldsymbol{n}}` is a unit vector perpendicular to the plane.

Coordinate Transformation in Euclidean Space
--------------------------------------------

To represent spatial motion and positioning, we use the :math:`D`-dimensional Euclidean space :math:`\mathbb{R}^D`. A position vector in :math:`3D` is written as:

.. math::

   \boldsymbol{x} = \begin{pmatrix}
   x_1 \\
   x_2 \\
   x_3
   \end{pmatrix} = \begin{pmatrix}
   x \\
   y \\
   z
   \end{pmatrix}.

For :math:`2D` and :math:`1D`, the coordinates are given as:

.. math::

   \boldsymbol{x}^T = \begin{pmatrix} x_1 & x_2 \end{pmatrix} = \begin{pmatrix} x & y \end{pmatrix}, \quad
   \boldsymbol{x}^T = \begin{pmatrix} x_1 \end{pmatrix} = \begin{pmatrix} x \end{pmatrix}.

**Gradient Operator**

In cylindrical coordinates, the gradient operator is:

.. math::

   \nabla = \begin{pmatrix}
   \frac{\partial}{\partial r} \\
   \frac{1}{r} \frac{\partial}{\partial \phi} \\
   \frac{\partial}{\partial z}
   \end{pmatrix}.

**Divergence and Curl**

For the divergence in cylindrical coordinates:

.. math::

   \nabla \cdot \boldsymbol{a} = \frac{1}{r} \frac{\partial (r a_r)}{\partial r} + \frac{1}{r} \frac{\partial a_\phi}{\partial \phi} + \frac{\partial a_z}{\partial z}.

For the curl in cylindrical coordinates:

.. math::

   \nabla \times \boldsymbol{a} = \begin{pmatrix}
   \frac{1}{r} \frac{\partial a_z}{\partial \phi} - \frac{\partial a_\phi}{\partial z} \\
   \frac{\partial a_r}{\partial z} - \frac{\partial a_z}{\partial r} \\
   \frac{1}{r} \left( \frac{\partial}{\partial r} (r a_\phi) - \frac{\partial a_r}{\partial \phi} \right)
   \end{pmatrix}.

