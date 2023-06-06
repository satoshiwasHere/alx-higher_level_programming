-- Script lists all cities contained in the database hbtn_0d_usa
SELECT cty.`id`, cty.`name`, state.`name`
  FROM `cities` AS cty INNER JOIN `states` AS state
       ON cty.`state_id` = state.`id`
 ORDER BY cty.`id`;
  
