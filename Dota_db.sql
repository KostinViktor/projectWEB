BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Hero" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"name"	TEXT NOT NULL,
	"build"	INTEGER NOT NULL,
	"spell"	INTEGER NOT NULL,
	FOREIGN KEY("build") REFERENCES "Build"("id"),
	FOREIGN KEY("spell") REFERENCES "Spell"("id")
);
CREATE TABLE IF NOT EXISTS "Spell" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"leveling"	TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS "Build" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"early"	TEXT NOT NULL,
	"midgame"	TEXT NOT NULL,
	"lategame"	TEXT NOT NULL
);
INSERT INTO "Hero" VALUES (1,'Sniper',1,1);
INSERT INTO "Hero" VALUES (2,'Axe',2,2);
INSERT INTO "Hero" VALUES (3,'Ogre Magi',3,3);
INSERT INTO "Hero" VALUES (4,'Sven',4,4);
INSERT INTO "Hero" VALUES (5,'Lich',5,5);
INSERT INTO "Hero" VALUES (6,'Lion',6,6);
INSERT INTO "Hero" VALUES (7,'Phantom Assassin',7,7);
INSERT INTO "Spell" VALUES (1,'WQEWERWEWERQQQR');
INSERT INTO "Spell" VALUES (2,'WEQEQREQEQQRWWWR');
INSERT INTO "Spell" VALUES (3,'QWQWQRQWEWREEER');
INSERT INTO "Spell" VALUES (4,'QEWWWRWQEQREQEER');
INSERT INTO "Spell" VALUES (5,'WEQWERWEWERQQQR');
INSERT INTO "Spell" VALUES (6,'QWEQWRQWQWREEER');
INSERT INTO "Spell" VALUES (7,'QWEQERQEQERWWWR');
INSERT INTO "Build" VALUES (1,'Wraith Band x2, Power Treads, Dragon Lance','Hurricane Pike, Mjolnir','Satanic, MKB, Daedalus');
INSERT INTO "Build" VALUES (2,'Ring of Tarasque,  Phase Boots, Blink Dagger','Crimson guard, Blade Mail','Assault Cuirass, Heart of Tarasque');
INSERT INTO "Build" VALUES (3,'Hand of Midas, Arcane Boots','Blink Dagger, Scythe of Vyse','Ethereal Blade, Octarine Core');
INSERT INTO "Build" VALUES (4,'Bracer, Power Treads, Echo Sabre','Blink Dagger, Crystals','Daedalus, Satanic, BKB');
INSERT INTO "Build" VALUES (5,'Arcane boots, Magic stick','Glimmer Cape, Force Staff','Aghanim''s Scepter, Ethereal Blade');
INSERT INTO "Build" VALUES (6,'Arcane Boots, Blink Dagger','Aghanim''s Scepter, Ethereal Blade','Octarine Core, Bloodstone');
INSERT INTO "Build" VALUES (7,'Wraith Band x2, Phase Boots','Desolator, BKB','Satanic, MKB, Daedalus');
CREATE INDEX IF NOT EXISTS "idx_hero__spell" ON "Hero" (
	"spell"
);
CREATE INDEX IF NOT EXISTS "idx_hero__build" ON "Hero" (
	"build"
);
COMMIT;
