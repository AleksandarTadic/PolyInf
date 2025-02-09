USE 2023_nosql_baza_cinjenica;

DROP PROCEDURE IF EXISTS DobaviPersonalniZadatak;
DELIMITER \
CREATE PROCEDURE DobaviPersonalniZadatak(in p1 char, in p2 int, in p3 char)
BEGIN
SELECT
	(SELECT PS_NAZIV FROM poslovni_subjekat WHERE poslovni_subjekat.DR_OZNAKA = isporuceno.POS_DR_OZNAKA AND poslovni_subjekat.PS_ID = isporuceno.PS_ID) AS NAZIV_KOMPANIJE_ISPORUCIOCA,
    isporuceno.PLA_ID AS PLASMAN_ID,
    (SELECT DR_NAZIV FROM drzava WHERE drzava.DR_OZNAKA = isporuceno.POS_DR_OZNAKA) AS NAZIV_DRZAVE_ISPORUCIOCA,
    (SELECT PS_NAZIV FROM poslovni_subjekat WHERE poslovni_subjekat.DR_OZNAKA = isporuceno.POS_DR_OZNAKA AND poslovni_subjekat.PS_ID = isporuceno.PS_ID) AS NAZIV_KOMPANIJE_ISPORUCIOCA,
    isporuceno.DR_OZNAKA,
    isporuceno.SPR_TIP AS TIP,
    drzava.DR_NAZIV AS PLASIRANO_DRZAVI,
    softverski_proizvod.SPR_NAZIV,
    isporuceno.SPR_KATBR,
    isporuceno.VER_OZNAKA,
    poslovni_subjekat.PS_NAZIV,
    poslovni_subjekat.PS_ADRESA,
    poslovni_subjekat.PS_WWW,
    isporuceno.PLA_GODINA,
    isporuceno.PLA_BROJ_PLASMANA,
    (SELECT poslovni_subjekat.PS_NAZIV FROM poslovni_subjekat WHERE poslovni_subjekat.DR_OZNAKA = plasman_konfiguracije.POS_DR_OZNAKA and poslovni_subjekat.PS_ID = plasman_konfiguracije.POS_PS_ID) AS DRZAVA_INVESTITOR,
    plasman_konfiguracije.PLA_DATUM_UG,
    isporuceno.PPL_RBR,
    isporuceno.PPL_PLANIRANO,
    isporuceno.PPL_REALIZOVANO
    
FROM
	isporuceno,
    poslovni_subjekat,
    konfiguracija,
    softverski_proizvod,
    plasman_konfiguracije,
    drzava
WHERE 
	-- (isporuceno.DR_OZNAKA = p1 AND isporuceno.PLA_PS_ID = p2 AND isporuceno.SPR_TIP = p3)
    (isporuceno.POS_DR_OZNAKA = p1 AND isporuceno.PS_ID = p2 AND isporuceno.SPR_TIP = p3)
    AND
    (isporuceno.DR_OZNAKA != isporuceno.POS_DR_OZNAKA)
	AND 
    (konfiguracija.SOF_DR_OZNAKA = isporuceno.SOF_DR_OZNAKA AND konfiguracija.POS_PS_ID = isporuceno.POS_PS_ID AND konfiguracija.SPR_KATBR = isporuceno.SPR_KATBR AND isporuceno.SPR_TIP = konfiguracija.SPR_TIP AND isporuceno.VER_OZNAKA = konfiguracija.VER_OZNAKA AND isporuceno.KONF_ID = konfiguracija.KONF_ID)
	AND 
    (softverski_proizvod.DR_OZNAKA = isporuceno.SOF_DR_OZNAKA AND isporuceno.POS_PS_ID = softverski_proizvod.POS_PS_ID AND isporuceno.SPR_KATBR = softverski_proizvod.SPR_KATBR AND isporuceno.SPR_TIP = softverski_proizvod.SPR_TIP)
    AND
    (poslovni_subjekat.DR_OZNAKA = isporuceno.POS_DR_OZNAKA AND poslovni_subjekat.PS_ID = isporuceno.PS_ID)
    AND
    (plasman_konfiguracije.DR_OZNAKA = isporuceno.DR_OZNAKA AND plasman_konfiguracije.PS_ID = isporuceno.PLA_PS_ID AND plasman_konfiguracije.PLA_GODINA = isporuceno.PLA_GODINA AND isporuceno.PLA_BROJ_PLASMANA = plasman_konfiguracije.PLA_BROJ_PLASMANA)
    AND 
    (drzava.DR_OZNAKA = isporuceno.DR_OZNAKA)
END
DELIMITER ;