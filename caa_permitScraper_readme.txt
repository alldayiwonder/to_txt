Background:
Industrial facilities that emit contaminants to the air in New York State, unless specifically exempted, are required to obtain a Title V permit, a state facility permit, or a registration certificate​ from the New York State Department of Environmental Conservation.

Issued permits become final after a required public notice and comment period and are renewed regularly. These documents hold a variety of information about the facility, including specifics on how pollution limitations, controls, and/or monitoring requirements. This information is used every day by organizations, government, researchers, and others to understand a given facility.

NYS permits are housed here: http://www.dec.ny.gov/chemical/32249.html

Problem:
These environmental permits hold important information and the data is not accessible in machine-readable format since there is no requirement yet at the State and Federal levels to release data in machine-readable formats. 

Outline of important information:
## typically on first page 
<permit type>
<permit id>
<permit issued to>
<facility name>
<facility address>
<facility contact>
<facility description>

## typically on a page entitled "list of conditions" 
<federally enforceable conditions>

## emission information
## if page with"Facility Permissible Emissions" exists then need:
<name of pollutant>  # written as "Name:"
<potential to emit>  # written as "PTE:" or "PTE(s):" and followed by value 

## "Emission Unit Permissible Emissions"
## if page with"Emission Unit Permissible Emissions" exists then need:
<emission unit>  # this should match up with the same emission unit and related information in subsequent pages below
<name of pollutant>  # written as "Name:"
<potential to emit>  # written as "PTE:" or "PTE(s):" and followed by value 

## in all subsequent pages 
## information on emission units, the equipment that releases pollution into the air 

<emission units>  # written as "Emission Unit: [unit id here]"
<emission unit description>  # written as "Emission Unit Description: [description here] and follows the above
<control type>  # written as "Control Type:" and not always present, depends on emission unit and may repeat multiple times, we only need it once 

## information on monitoring requirements 

<monitoring type>  # written as "Monitoring Type:"
<monitoring frequency>  # written as "Monitoring Frequency:"
<parameter monitored>  # written as "Parameter Monitored:" and not always present, it depends on monitoring type
<upper permit limit>  # written as "Upper Permit Limit:" and not always present, depends on monitoring type
<lower permit limit>  # written as "Lower Permit Limit:" and not always present, depends on monitoring type
