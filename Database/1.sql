-- Column: public."Standards "."ID"

-- ALTER TABLE IF EXISTS public."Standards " DROP COLUMN IF EXISTS "ID";

ALTER TABLE IF EXISTS public."Standards"
    DROP COLUMN IF EXISTS "ID";

ALTER TABLE IF EXISTS public."Standards"
    ADD COLUMN "ID" SERIAL PRIMARY KEY;