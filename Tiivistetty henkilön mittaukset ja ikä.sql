DROP VIEW "main"."henkilo_mittaus_ika_v2";
CREATE VIEW henkilo_mittaus_ika_v2 AS
SELECT henkilo.henkilo_id, henkilo.sukunimi, henkilo.etunimi, mittaus.mittaus_id, henkilo.sukupuoli, mittaus.pituus, mittaus.paino, (julianday('now') - julianday(henkilo.spaiva))/365 AS ika
FROM henkilo INNER JOIN mittaus ON henkilo.henkilo_id = mittaus.henkilo_id