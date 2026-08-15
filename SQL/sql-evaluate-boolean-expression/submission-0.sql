-- Write your query below
select 
    x.left_operand,
    --v.value  as left_value,
    x.operator,
    x.right_operand,
    --vv.value as right_value,
    case when operator = '<' and v.value < vv.value then true
    when operator = '=' and v.value = vv.value then true
    when operator = '>' and v.value > vv.value then true
    else false end as value

from 
expressions x  join variables v on x.left_operand = v.name 
 join variables vv on x.right_operand = vv.name