
-- 查出至少有一个员工的部门。显示部门编号、部门名称、部门位置、部门人数。
SELECT d.deptno,d.dname,d.loc,COUNT(*) 
FROM t_dept d,t_employees e
WHERE e.deptno=d.deptno;
-- 列出所有员工的姓名及其直接上级的姓名。
SELECT e.empno,e.ename,e.deptno 
FROM t_employees e,t_employees m
WHERE e.MGR=m.empno AND e.hiredate<m.hiredate
-- 列出部门名称和这些部门的员工信息，同时列出那些没有员工的部门
SELECT * 
FROM t_employees e 
RIGHT OUTER JOIN t_dept d ON e.deptno=d.deptno
-- 列出最低薪金大于15000的各种工作及从事此工作的员工人数。
SELECT job,COUNT(*) 
FROM t_employees e 
GROUP BY job HAVING MIN(sal)>15000
-- 列出在销售部工作的员工的姓名，假定不知道销售部的部门编号。
SELECT *
FROM t_employees e
WHERE e.deptno=(SELECT deptno FROM t_dept WHERE dname='acountint')
-- 列出薪金高于公司平均薪金的所有员工信息，所在部门名称，上级领导，工资等级。
SELECT e.*,d.dname,m.ename
FROM t_employees e,t_dept d,t_employees m
WHERE e.sal>(SELECT AVG (sal) FROM t_employees) AND e.deptno = d.deptno AND e.mgr = m.empno AND e.sal
-- 列出与荀彧从事相同工作的所有员工及部门名称
SELECT e.*,d.dname 
FROM t_employees e, t_dept d 
WHERE e.deptno=d.deptno AND job=(SELECT job FROM t_employees WHERE ename="荀彧")
-- 列出薪金高于在部门30工作的所有员工的薪金的员工姓名和薪金、部门名称
SELECT e.ename, e.sal, d.dname
FROM t_employees e, t_dept d
WHERE e.deptno=d.deptno AND sal > ALL (SELECT sal FROM t_employees WHERE deptno=30) 


