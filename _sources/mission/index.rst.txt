:navigation: header
:order: 10

=======
mission
=======

``geometor.petersen`` establishes a rigorous Digital Scriptorium Book Codex and exact symbolic pattern library for **Julius Petersen's** *Methods and Theories for the Solution of Problems of Geometrical Constructions, Applied to 410 Problems* (1866 / 1879) as the methodological and heuristic bridge of the **GEOMETOR** constructive canon.

Core Objectives
---------------

1. **Systematizing Geometric Discovery (*Ars Inveniendi*)**: Where Euclid's *Elements* (``geometor/euclid``, ``geometor/elements``) presents finished deductive proofs, Petersen reveals the *analytic engine* that discovers constructions: relaxing a single condition to generate **Point Loci** (``a``–``k``), **Tangential Line Loci** (``l``–``p``), or **Positional Homothety**, and applying invertible **Transformations of the Figure** (**Parallel Translation**, **Replacing**, **Axial Reflection**, **Spiral Revolution**, and **Circle Inversion**) to gather dispersed data into constructible triangles.
2. **100% Exact Symbolic Realization** (``geometor.model``): Every flagship heuristic pattern is accompanied by an exact, float-free SymPy construction in :mod:`geometor.petersen.constructions`—built with ``Model(..., auto_intersect=False)``, explicit ``intersect`` / ``subconstruction`` DAGs, ``@proposition`` verification, and Rational Trigonometry invariants (``quadrance``, ``line_spread``, ``cross_ratio``), while keeping the historical Book Codex tracks strictly free of embedded ``py_file`` scripts.
3. **Cross-Corpus Lineage**: Map Petersen's 1866/1879 methods backward to Euclid and Pappus (*Synagoge* Book VII) and forward to Émile Lemoine (*Géométrographie*, 1902), David Hilbert (*Grundlagen der Geometrie* Ch. VII, 1899), Nathan Altshiller-Court (*College Geometry*, 1925/1952), George Pólya (*How to Solve It*, 1945), and Clark Kimberling's *Encyclopedia of Triangle Centers* (``geometor/etc``).
