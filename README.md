ArcGIS_BiomassCostTool
======================

The Biomass Cost Analyst Tool estimates a price per ton of woody biomass for each inventory stand. It takes into account the stumpage price for each individual stratum, the harvest costs, the reforestation costs, and the transportation costs to a determined location.

It requires several input data:
* an inventory Layer;  containing the individual stands with the corresponding tons per acre, the tons, and the acre of the stand. 
* a point that determines the destination to where the biomass shall be transported to
* polygons, that cover operable areas, points that determine the road access to the areas, as well as the distance from these points to the destination (this is optinal)

The tool can be added to the ArcToolbox in ArcMap 10.0, or in ArcCatalog 10.0, and requires an ArcInfo License. It was created with the ModelBuilder application in ArcGIS, and with Python scripts, that were integrated into the model.

-------------------


Information on how to use the tool can be found in the help file after downloading the tool and starting it in ArcGIS.

Information about the background of the tool can be found in this [publication] (http://gispoint.de/index.php?id=5&tx_browser_pi1%5Bsword%5D=strötz&tx_browser_pi1%5BnewsUid%5D=692&cHash=6537b0bfeb#!).

