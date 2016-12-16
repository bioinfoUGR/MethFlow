<h3>Introduction</h3>
MethFlow is an optimized, open-source pipeline which performs DNA methylation profiling, detection of sequence variants, full integration with our methylation database, <em>NGSmethDB</em>, and differential methylation analysis. Briefly, the pipeline performs the following steps:
<ol>
 	<li>Format conversion: convert SRA files to FASTQ by means of <em>SRA Toolkit</em>. This only applies if the input data comes from Sequence Read Archive (SRA) public repository.</li>
 	<li>Adapter and low quality bases trimming by means of <em>Trimmomatic</em>.</li>
 	<li>Alignment against one or two assemblies: firstly, short reads are aligned against the first assembly (assembly 1 from now on) producing uniquely-mapped, multiple-mapped and unmapped reads. Uniquely-mapped reads are kept to use in the next step. Secondly, multiple-mapped and/or unmapped reads are aligned against the second assembly (assembly 2 from now on) producing uniquely-mapped, multiple-mapped and unmapped reads. Uniquely-mapped reads are merged with previously obtained uniquely-mapped reads and used in the next step. <em>Bismark</em> is used as aligner.</li>
 	<li>Elimination of known technical artifacts by <em>BSeQC</em>.</li>
 	<li>Detection of DNA methylation and sequence variants by <em>MethylExtract</em>.</li>
 	<li>Get methylation maps from NGSmethDB.</li>
 	<li>Differential methylation analysis by <em>methylKit</em> and <em>MOABS</em> and generate a consensus of both.</li>
</ol>
<em>MethFlow</em> pipeline was inplemented in three ways. We first provide the software optimized to run in a powerful and user-friendly cloud environment. Second, for users requiring the maximal level of data privacy, we developed <em>MethFlow<sup>VM</sup></em>, a ready-to-use, fully-configured virtual machine which is able to run on most operating systems (Windows, Linux or Mac). With <em>MethFlow<sup>VM</sup></em> the user will no longer need to upload private data to any public server. Finally, advanced users can download the source code from a public repository, which allows installing and customizing <em>MethFlow</em> on any operating system. See <a href="http://bioinfo2.ugr.es:8080/MethFlow/download/" target="_blank">Links and downloads</a> for links to connect to the cloud app or to download the virtual machine or the standalone programs. The cloud app contains an intuitive menu which facilitates its use. The following instructions are for the command line of the VM and standalone programs.
<h3><span id="noHighlight_0.7529770015681014"></span>The local database</h3>
<h4><strong>Set your working folder</strong></h4>
At first startup, you will be asked which working folder you want to use. If you ignore this question, your home folder (<em>/home/methflow </em>in MethFlow<sup>VM</sup>) will be used as working folder. We strongly recommended to use a shared folder as working folder.

If you want to change the working folder, open a terminal and type the following command:
<pre style="text-align: center;"><strong>MethFlow_manager working_folder</strong></pre>
<h4><strong>Set your assembly collection</strong></h4>
Tell MethFlow where the assembly collection is by typing:
<pre style="text-align: center;"><strong>MethFlow_manager assembly_collection Assemblies</strong></pre>
<p style="text-align: left;">This command looks for a folder named <em>Assemblies</em> inside the working folder. If the desired folder is outside the working folder, use the <strong>‐‐out </strong>option.</p>

<h4><strong>Set your adapter collection</strong></h4>
Tell MethFlow where the adapter collection is by typing:
<pre style="text-align: center;"><strong>MethFlow_manager adapter_collection Adapters</strong></pre>
This command looks for a folder named <em>Adapters</em> inside the working folder. If the desired folder is outside the working folder, use the <strong>‐‐out </strong>option.
<h4><strong>Set your root input folder</strong></h4>
Tell MethFlow where to look for the input folders:
<pre style="text-align: center;"><strong>MethFlow_manager root_input_folder Inputs</strong></pre>
<p style="text-align: left;">This command looks for a folder named <em>Inputs</em> inside the working folder. If the desired folder is outside the working folder, use the <strong>‐‐out </strong>option.</p>

<h4><strong>Set your root output folder</strong></h4>
Tell MethFlow where to kept the output folders:
<pre style="text-align: center;"><strong>MethFlow_manager root_output_folder Outputs</strong></pre>
<p style="text-align: left;">This command creates a folder named <em>Outputs</em> inside the working folder. If the desired folder is outside the working folder, use the <strong>‐‐out </strong>option.</p>

<h4><strong>Set intermediates folder</strong></h4>
Tell MethFlow where to kept the intermediates output folders:
<pre style="text-align: center;"><strong>MethFlow_manager intermediates_folder Intermediates</strong></pre>
<p style="text-align: left;">This command creates a folder named <em>Intermediates</em> inside the root output folder. If the desired folder is outside the root output folder, use the <strong>‐‐out </strong>option.</p>

<h4><strong>Set plots folder</strong></h4>
Tell MethFlow where to kept the plots output folders:
<pre style="text-align: center;"><strong>MethFlow_manager plots_folder Plots</strong></pre>
<p style="text-align: left;">This command creates a folder named <em>Plots</em> inside the root output folder. If the desired folder is outside the root output folder, use the <strong>‐‐out </strong>option.</p>

<h4><strong>Set meth folder</strong></h4>
Tell MethFlow where to kept the methylation maps:
<pre style="text-align: center;"><strong>MethFlow_manager meth_folder Meth</strong></pre>
<p style="text-align: left;">This command creates a folder named <em>Meth</em> inside the root output folder. If the desired folder is outside the root output folder, use the <strong>‐‐out </strong>option.</p>

<h4><strong>Set diffmeth folder</strong></h4>
Tell MethFlow where to kept the differential methylation maps:
<pre style="text-align: center;"><strong>MethFlow_manager diffmeth_folder Diffmeth</strong></pre>
<p style="text-align: left;">This command creates a folder named <em>Diffmeth</em> inside the root output folder. If the desired folder is outside the root output folder, use the <strong>‐‐out </strong>option.</p>

<h3><strong>Launch MethFlow</strong></h3>
<h4>Using default options</h4>
Now, launch MethFlow with default options:
<pre style="text-align: center;"><strong>MethFlow</strong></pre>
This command looks inside the working folder and asks you for:
<ol>
 	<li><strong>Assembly 1 folder.</strong> This folder should contain FASTA or multiFASTA files and must be inside the assembly collection folder. Optionally, it could contain Bismark Bowtie2 indexes.</li>
 	<li><strong>Adapter file.</strong> This file must be a multiFASTA file inside the adapter collection.</li>
 	<li><strong>Input data folder.</strong> This folder should contain all the input datasets of a sample in SRA, FASTQ, SAM or BAM format (all files must be in the same format) and must be inside the root input folder.</li>
 	<li><strong>Output data folder.</strong> This folder will be create inside the root output folder.</li>
</ol>
Methylation maps calculated by MethFlow are located at meth folder inside the root output folder.
<h4>Using two assemblies</h4>
If you want to use a second assembly, launch MethFlow as follow:
<pre style="text-align: center;"><strong>MethFlow ‐‐assembly2</strong></pre>
In this case, MethFlow asks you for:
<ol>
 	<li><strong>Assembly 1 folder.</strong> This folder should contain FASTA or multiFASTA files and must be inside the assembly collection folder. Optionally, it could contain Bismark Bowtie2 indexes.</li>
 	<li><strong>Assembly 2 folder.</strong> This folder should contain FASTA or multiFASTA files and must be inside the assembly collection folder. Optionally, it could contain Bismark Bowtie2 indexes.</li>
 	<li><strong>What type of reads you want to use against the assembly 2:</strong> multiple-mapped reads, unmapped reads or both.</li>
 	<li><strong>Adapter file.</strong> This file must be a multiFASTA file inside the adapter collection.</li>
 	<li><strong>Input data folder.</strong> This folder should contain all the input datasets of a sample in SRA, FASTQ, SAM or BAM format (all files must be in the same format) and must be inside the root input folder.</li>
 	<li><strong>Output data folder.</strong> This folder will be create inside the root output folder.</li>
</ol>
Methylation maps calculated by MethFlow are located at meth folder inside the root output folder.
<h4>Enable NGSmethDB API client</h4>
<span id="ouHighlight__16_18TO14_16" class="">Use</span><span id="noHighlight_0.0906570260582924"> </span><span id="ouHighlight__20_22TO18_20">the</span><span id="noHighlight_0.5782996075823763"> </span><span id="ouHighlight__24_31TO22_28">option</span><span id="noHighlight_0.14885440070328393"> <strong>‐‐enable_api</strong></span><span id="noHighlight_0.11344022272910004"> </span><span id="ouHighlight__41_44TO42_43">to</span><span id="noHighlight_0.7456307411930678"> </span><span id="ouHighlight__46_52TO45_52">activate</span><span id="noHighlight_0.6097980775447114"> NGSmethDB API client</span><span id="noHighlight_0.19534596049887143"> </span><span id="noHighlight_0.3839531351818044">functionaly</span><span id="noHighlight_0.6297298994401557">.</span><span id="noHighlight_0.5849362428588822"> </span><span id="ouHighlight__78_85TO77_84">MethFlow asks </span><span id="noHighlight_0.8807107168266013"></span><span id="ouHighlight__87_88TO86_88">you</span><span id="noHighlight_0.9520375869905775"> </span><span id="ouHighlight__101_103TO97_100">what</span><span id="noHighlight_0.4112756769424726"> </span><span id="ouHighlight__105_112TO102_108" class="">samples</span><span id="noHighlight_0.9787954657415041"> you want to </span><span id="ouHighlight__114_122TO110_117" class="">download</span><span id="noHighlight_0.5888984200260194"> from</span><span id="noHighlight_0.2157172174708979"> </span><span id="ouHighlight__127_128TO122_124">the</span><span id="noHighlight_0.33090849979118264"> </span><span id="ouHighlight__130_138TO126_134">NGSmethDB</span><span id="noHighlight_0.9979496553751572">. Methylation maps downloaded from NGSmethDB are located at meth folder inside the root output folder.</span>
<h4>Enable differential methylation analysis</h4>
<span id="ouHighlight__16_18TO14_16" class="">Use</span><span id="noHighlight_0.0906570260582924"> </span><span id="ouHighlight__20_22TO18_20">the</span><span id="noHighlight_0.5782996075823763"> </span><span id="ouHighlight__24_31TO22_28">option</span><span id="noHighlight_0.8178921835612691"> <strong>‐‐enable_diffmeth</strong></span><span id="noHighlight_0.5483406972786837"> </span><span id="ouHighlight__41_44TO42_43">to</span><span id="noHighlight_0.7456307411930678"> </span><span id="ouHighlight__46_52TO45_52">activate</span><span id="noHighlight_0.6097980775447114"> </span><span id="noHighlight_0.3839531351818044">differential methylation analysis functionaly</span><span id="noHighlight_0.6297298994401557">.</span><span id="noHighlight_0.5849362428588822"> </span><span id="ouHighlight__78_85TO77_84">MethFlow asks </span><span id="noHighlight_0.8807107168266013"></span><span id="ouHighlight__87_88TO86_88">you</span><span id="noHighlight_0.9520375869905775"> </span><span id="noHighlight_0.14002499373866995">what</span><span id="noHighlight_0.5886416442989675"> </span><span id="ouHighlight__146_153TO145_151">samples</span><span id="noHighlight_0.9673121861636826"> </span><span id="ouHighlight__155_162TO153_159">compare </span><span id="noHighlight_0.4510468058318138"></span><span id="ouHighlight__164_165TO161_162">in</span><span id="noHighlight_0.9755744369350245"> </span><span id="ouHighlight__167_168TO164_166" class="">the </span><span id="ouHighlight__193_203TO192_203" class="">differential<span id="noHighlight_0.2595808121142329"> </span><span id="ouHighlight__182_191TO180_190" class="">methylation</span><span id="noHighlight_0.7804256309098638"> </span>analysis</span><span id="noHighlight_0.9979496553751572">. Differential methylation maps calculated by MethFlow are located at Diffmeth folder inside the root output folder.</span>

---
<h3>Analyze the results files</h3>
The output folder of every analyzed input sample directory contains a number of folders:
<ul>
 	<li><strong>Methylation_Maps folder.</strong> With three folders inside:
<ul>
 	<li><strong>MethylExtract folder.</strong> It contains between one to three methylation map files, one for each analyzed methylation context (see <a href="#toc-Section-5"><em>Change parameters and launch options</em></a>): <strong><em>CG.output</em></strong>, <strong><em>CHG.output</em></strong> and <strong><em>CHH.output</em></strong>. These files contain the methylation profiling results at a single cytosine resolution: the methylation context, the position on the genome, the number of reads where this cytosine is methylated, the coverage and the sequencing quality. For a full description of this format visit <a href="http://bioinfo2.ugr.es/MethylExtract/downloads/ManualMethylExtract.pdf">the manual of MethylExtract</a>.</li>
 	<li><strong>methylKit folder.</strong> The methylation profiling results in methylKit input format. This format can also be used by <a href="http://sartorlab.ccmb.med.umich.edu/node/17">MethylSig</a>. For a full description of this format visit <a href="http://rpubs.com/al2na/methylKit">the manual of methylKit</a>.</li>
 	<li><strong>methylKit_plots folder.</strong> The methylation ratio and coverage distributions of the input sample, plotted by methylKit. Files are in PDF format. To get these plots in other formats, see <a href="#toc-Section-6"><em>Downstream analysis</em></a>.</li>
</ul>
</li>
 	<li><strong>Differential_Methylation_Maps folder.</strong> With three folders inside:
<ul>
 	<li><strong>methylKit_DMC_maps.</strong> It contains one file for each pair of methylation maps analysed.</li>
 	<li><strong>MOABS_DMC_maps.</strong> It contains one file for each pair of methylation maps analysed.</li>
 	<li><strong>consensus_DMC_maps.</strong> It contains one file for each pair of methylation maps analysed.</li>
</ul>
</li>
</ul>
<ul>
 	<li><strong>SNVs folder.</strong> There is only one file here: <strong><em>SNVs.vcf</em></strong>. This file contains the sequence variants detected in the input sample against the reference genome assembly. The VCF format specifications can be seen <a href="http://samtools.github.io/hts-specs/VCFv4.3.pdf">here</a>.</li>
 	<li><strong>Logs folder.</strong> Contains a folder for each program used during the pipeline. Each of these folders have two logs for every processed file: one log recording the standard output and the other recording the standard error.</li>
 	<li><strong>CITE.txt file.</strong> A text file within the references that you should cite if you use MethFlow, including all references to third-party software used in a particular process.</li>
 	<li><strong>FASTQ folder (for SRA input files).</strong> It stores the FASTQ files converted from the original SRA files. There will be either one or two FASTQ files for each SRA file, depending whether the sequencing reads are single-end or paired-end. Only if input sample is SRA or FASTQ and <strong><em>--adapters_trimmed</em></strong> is not specified.</li>
 	<li><strong>trimmed_FASTQ folder.</strong> It stores the trimmed FASTQ files, i.e. the Trimmomatic output files. Only if input sample format is SRA or FASTQ.</li>
 	<li><strong>FastQC folder.</strong> With two folders inside:
<ul>
 	<li><strong>FASTQ_FASTQC folder.</strong> Contains the quality report of the FASTQ files before trimming. There is one report for each FASTQ file. Only if input sample format is SRA or FASTQ.</li>
 	<li><strong>trimmed_FASTQ_FastQC folder.</strong> Contains the quality report of the FASTQ files after trimming. There is one report for each FASTQ file. Only if input sample is SRA or FASTQ and <strong><em>--adapters_trimmed</em></strong> is not specified.</li>
</ul>
</li>
 	<li><strong>ambiguous_FASTQ folder.</strong> It stores the FASTQ files ambiguously mapped against the first assembly. There is one file for each FASTQ used during alignment against the first assembly. This folder appears if the input format is SRA or FASTQ and a second assembly is used.</li>
 	<li><strong>unmapped_FASTQ folder.</strong> It stores the FASTQ files with unmapped reads against the first assembly. There is one file for each FASTQ used during alignment against the first assembly. This folder appears if the input format is SRA or FASTQ and a second assembly is used.</li>
 	<li><strong>BAM folder.</strong> Contains BAM files coming from alignment against the first assembly and, if applicate, the second assembly. There is only one file for each dataset (paired-end data no longer have two files). BAM files from second assembly alignment are merged, if applicable. Only if input sample format is SRA or FASTQ.</li>
 	<li><strong>fixed_SAM folder.</strong> Contains SAM files after bisulfite bias fixing. There is only one file for each dataset. Only if <strong><em>--bisulfite_bias_fixed</em></strong> is not set on the command line.</li>
 	<li><strong>BSeQC_plots folder.</strong> Contains plots about the bisulfite bias. There is only one folder for each dataset. Only if <strong><em>--bisulfite_bias_fixed</em></strong> is not set on the command line.</li>
</ul>
<h3>Local settings</h3>
The easiest way to use MethFlow is to set the value of certain parameters by means of a setting file. This file can be found within your home: <strong><em>$HOME/.methflowrc</em></strong> (note the dot at the beginning), where <em>$HOME</em> is your home directory (i.e. <em>/home/methflow</em>). It is not listed with <em>ls</em>, except you add the option <em>-a</em>.

This file is a text file that can be edited with any plain text editor such as vim or nano:
<pre style="text-align: center;"><strong><em>nano $HOME/.methflowrc</em></strong></pre>
It should contain eight variables:
<ul>
 	<li><strong>working:</strong> the path of the shared folder to be used.</li>
 	<li><strong>assemblies:</strong> the path of the assemblies folder (see <a href="http://bioinfo2.ugr.es:8080/MethFlow/wp-admin/post.php?post=1220&amp;action=edit#toc-Subsection-4.3"><em>Set assemblies folder</em></a>).</li>
 	<li><strong>adapters:</strong> the path of the adapter collection.</li>
 	<li><strong>output:</strong> the path of the base output folder.</li>
 	<li><strong>intermediates:</strong> the path where intermediates output files were kept.</li>
 	<li><strong>plots:</strong> the path where plots output files were kept.</li>
 	<li><strong>meth: </strong> the path where methylation maps were kept.</li>
 	<li><strong>diffmeth:</strong> the path where differential methylation maps were kept.</li>
</ul>
You can modify the variables. If the specified path does not exist or if the parameter is missing at all, MethFlow will ask again on the command line.
<h4><strong>Input data</strong></h4>
It is highly recommended to provide the input data from the shared folder. The data from different samples must go into separate folders. The input files located within the same folder are interpreted as different runs from the same sample. Accepted formats are <strong>SRA</strong>, <strong>FASTQ</strong>, <strong>SAM</strong> and <strong>BAM</strong>.

The directory with the sample dataset to be used can be specified in a configuration file (<strong>not to be confused with the settings file</strong>, see <a href="http://bioinfo2.ugr.es:8080/MethFlow/wp-admin/post.php?post=1220&amp;action=edit#toc-Subsection-4.1"><em>Local settings</em></a>) or on the command line when you launch MethFlow (see <a href="http://bioinfo2.ugr.es:8080/MethFlow/wp-admin/post.php?post=1220&amp;action=edit#toc-Subsection-5"><em>Change parameters and launch options</em></a>). Otherwise, you will be asked.
<h4><strong>Prepare the assemblies</strong></h4>
Each assembly must go into a separate folder into the assemblies folder. The assembly may consist of a multi-FASTA file or several FASTA files, all contained in the same directory. It may contain or not Bismark Bowtie2 indexes. If not, Bismark Bowtie2 indexes will be calculated during the first usage of the assembly by MethFlow.

The directory with the assembly can be specified in a configuration file (<strong>not to be confused with the settings file</strong>) or on the command line when you launch MethFlow (see <a href="http://bioinfo2.ugr.es:8080/MethFlow/wp-admin/post.php?post=1220&amp;action=edit#toc-Section-5"><em>Change parameters and launch options</em></a>). Otherwise, you will be asked.

You can download some assemblies (including Bismark Bowtie2 indexes) with this command:
<pre style="text-align: center;"><strong><em>MethFlow_manager get_assemblies</em></strong></pre>
The data is then downloaded to the assemblies folder set in <strong><em>.methflowrc</em></strong>.
<h3>Launch options</h3>
To run the MethFlow pipeline we execute the command <strong><em>MethFlow [arguments]</em></strong> together with the relevant arguments. If you do not specify any arguments the program will enter in the quick mode, where you will be asked interactively.
There is an auxiliar command, MethFlow_configure [arguments], which can be used to create a configuration file (<strong>not to be confused with the settings file</strong>). This command does not launch MethFlow but it generates a configuration file with the parameters specified on the command.
MethFlow can be used in three ways:
<ul>
 	<li><strong>Interactive: <em>MethFlow</em></strong>. The program asks you the mandatory arguments through dialogs.</li>
 	<li><strong>Configuration file:</strong> you indicate arguments to be used in a configuration file created by MethFlow and edited by you. Type <strong><em>MethFlow --config configuration_file</em></strong> to use this mode, where <strong><em>configuration_file</em></strong> is the configuration file previously generated by MethFlow or edited by you.</li>
 	<li><strong>Command line: <em>MethFlow [arguments]</em></strong>. The arguments are given when launching the program. If any mandatory arguments are missing you will be asked interactively. It can be combined with the configuration file mode. In case of conflict, the command line value of the conflictive argument will be used.</li>
</ul>
<h4>Mandatory arguments</h4>
Some parameters must be indicated by the user:
<ul>
 	<li><strong>input:</strong> the path of the input data folder. It must be indicated in a configuration file, on the command line or through a dialog. During the pipeline various arguments are detected: format of the input files, if they have single-end or paired-end reads, if they use phred33 or phred64 and the maximum and the minimum read length.</li>
 	<li><strong>adapters:</strong> the path of the adapter collection. It must be indicated in the <strong><em>settings file</em></strong>, in a configuration file, on the command line or through a dialog.</li>
 	<li><strong>assembly:</strong> the path of the first assembly folder. It must be indicated in a configuration file, on the command line or through a dialog. During the pipeline it is checked for Bismark Bowtie2 indexes. If there are not indexes within the folder, they will be calculated.</li>
 	<li><strong>output:</strong> the path of the base output folder. It must be indicated in the <strong><em>settings file</em></strong>, in a configuration file, on the command line or through a dialog.</li>
</ul>
If <strong><em>--assembly2</em></strong> is used there will be two extra mandatory arguments:
<ul>
 	<li><strong>&lt;assembly2_path&gt;:</strong> the path of the second assembly folder. It must be indicated in a configuration file, on the command line or through a dialog. During the pipeline it is checked for Bismark Bowtie2 indexes. If there are not indexes within the folder, they will be calculated.</li>
 	<li><strong>use_assembly2_for:</strong> indicates which kind of reads will be used for the mapping against the second assembly (ambiguously mapped reads against first assembly, unmapped reads or both). It must be indicated in a configuration file, on the command line or through a dialog. For example, to use it at the command line:</li>
</ul>
<pre style="text-align: center;"><strong><em>MethFlow --assembly2 &lt;assembly2_path&gt; --use_assembly2_for [ambiguous, unmapped or both]</em></strong></pre>
where <b><i>&lt;assembly2_path&gt;</i></b> is the path in the virtual machine for the assemblies you want to use. <strong>It is highly recommended that the assemblies folder is within the shared folder.</strong>

In addition, in this command, you have to chooses using <strong><em>ambiguous</em></strong>, <strong><em>unmapped</em></strong> or <strong><em>both</em></strong> kinds of reads.
<h4>Optional arguments</h4>
Most arguments are optional. When they are not given, MethFlow either calculates or tries to estimate them (like <em>minimum_read_length</em> and <em>threads</em>) or it uses the default values. Note that when the parameters are use on the command line, <strong><em>‘--‘</em></strong> must precede the parameter name. For example, parameter name: <strong><em>‘adapter_trimmed’</em></strong> ➜ on command line: <strong><em>--adapter_trimmed</em></strong>.
<ul>
 	<li><strong>adapter_trimmed:</strong> it is a bool argument <strong>(default: off)</strong>. When on, the adapters trimming is skipped.</li>
 	<li><strong>bisulfite_bias_fixed:</strong> it is a bool argument <strong>(default: off)</strong>. When on, the bisulfite bias fixing is skipped.</li>
 	<li><strong>library:</strong> indicates whether the type of sequencing library is directional, non-directional or PBAT <strong>(options: directional, non_directional or pbat;default: directional)</strong>. Unfortunately, this argument cannot be estimated before aligning. <strong>If you observe a high number of unmapped reads, try changing this argument.</strong></li>
 	<li><strong>rrbs:</strong> it is a bool argument <strong>(default: off)</strong>. Indicate that the sequencing technique used is Reduced Representation Bisulfite Sequencing (RRBS). It takes into account when bisulfite bias fixing. <strong>It is recommended to use combined with the argument not_remove_duplicate.</strong></li>
 	<li><strong>not_seed_mismatch:</strong> it is a bool argument <strong>(default: off)</strong>. When on, you do not use mismatches in seed during aligning. When off, you use one mismatch.</li>
 	<li><strong>seed_length:</strong> indicate the length of the seed used during aligning <strong>(minimum: 8; maximum: 32; default: 32)</strong>.</li>
 	<li><strong>not_remove_duplicate:</strong> it is a bool argument <strong>(default: off)</strong>. When on, duplicate reads are not remove during profiling. <strong>Recommended for RRBS data.</strong></li>
 	<li><strong>minimum_phred_score:</strong> indicate the minimum accepted phred score during trimming and profiling <strong>(default: 20)</strong>. To set separately for both steps, use advanced arguments (see <a href="http://bioinfo2.ugr.es:8080/MethFlow/wp-admin/post.php?post=1220&amp;action=edit#toc-Subsection-5.4"><em>Manipulate the configuration file</em></a>).</li>
 	<li><strong>minimum_read_length:</strong> indicate the minimum accepted read length during trimming <strong>(default: calculated as half of the original length of the reads)</strong>.</li>
 	<li><strong>minimum_coverage:</strong> indicate the minimum accepted coverage during profiling <strong>(default: 1)</strong>.</li>
 	<li><strong>methylation_context:</strong> indicate the methylation context to analysis during profiling <strong>(options: CG, CHG, CHH or ALL; default: CG)</strong></li>
 	<li><strong>threads:</strong> indicate the maximum number of threads to be used <strong>(default: calculated as the number of CPUs of the virtual machine; minimum: 2)</strong>.</li>
 	<li><strong>intermediates: </strong>indicate the path where intermediates output files were kept <strong>(default: as part of output folder)</strong>.</li>
 	<li><strong>disable_plots:</strong> a boolean option to switch off the plotting functions <strong>(not used by default)</strong>.</li>
 	<li><strong>plots:</strong> indicate the path where plots output files were kept<strong> (default: as part of output folder)</strong>.</li>
 	<li><strong>methylomes:</strong> indicate the path where methylation maps were kept <strong>(default: as part of output folder).</strong></li>
 	<li><strong>diffmeth: </strong>indicate the path where differential methylation maps were kept<strong> (default: as part of output folder)</strong>.</li>
 	<li><strong>enable_api:</strong> a boolean option to switch on the using of NGSmethDB API client <strong>(not used by default)</strong>.</li>
 	<li><strong>api_conf:</strong> use a NGSmethDB API configuration file instead of asking for the samples to download <strong>(not used by default)</strong>.</li>
</ul>
<h4>Use command line arguments</h4>
All arguments described above can be used in the command to run or configure MethFlow, adding a double hyphen before the name of the argument. For example:

<strong><em>--input &lt;path&gt;</em></strong>, <strong><em>--adapter_trimmed</em></strong>, <strong><em>--library non_directional</em></strong> or <strong><em>--threads 16</em></strong>.

If you run MethFlow without specify a configuration file, you will be asked for all mandatory arguments not specified on the command line or on the settings file. Optional arguments not indicated will take their default value.
<h3>Downstream analysis</h3>
In this section, we explain how to do serveral downstream analysis with the virtual machine and standalone implementations.
<h4><strong>methylKit downstream analysis</strong></h4>
Using methylKit you can do a lot of downstream analysis, as compare methylation maps of different samples by means of a Pearson correlation matrix and sample clustering.

MethFlow converts automatically the methylation maps from MethylExtract output format to methylKit input format during the pipeline (see <a href="http://bioinfo2.ugr.es:8080/MethFlow/wp-admin/post.php?post=1220&amp;action=edit#toc-Section-3"><em>Analyze the result files</em></a>). Anyway, you can convert MethylExtract output files into methylKit input files anytime by typing this command:
<pre style="text-align: center;"><strong><em>me2mk -i MethylExtract_Output_File -o methylKit_Input_File -c Methylation_Context (CG, CHG or CHH) [--destrand]</em></strong></pre>
<strong>-i</strong>, <strong>-o</strong> and <strong>-c</strong> are mandatory arguments. Optionally, you can use <strong>--destrand</strong> to merge the data from both Watson and Crick strands <strong>(default: off)</strong>.

To do a quick descriptive analysis using methylKit you can use the following commands:
<ul>
 	<li><strong>Methylation ratio distribution:</strong></li>
</ul>
<pre style="text-align: center;"><strong><em>mk_methRatio_distribution -i methylKit_Input_File -o Image_Ouput_File [-f format (pdf, ps, svg, png, jpeg, bmp or tiff)] [-a assembly] [-m methylation_context]</em></strong></pre>
<strong>-i</strong> and <strong>-o</strong> are mandatory arguments. <strong>-f</strong> takes <strong>pdf</strong> as default value.
<ul>
 	<li><strong>Coverage distribution:</strong></li>
</ul>
<pre style="text-align: center;"><strong><em>mk_coverage_distribution -i methylKit_Input_File -o Image_Ouput_File [-f format (pdf, ps, svg, png, jpeg, bmp or tiff)] [-a assembly] [-m methylation_context]</em></strong></pre>
<strong>-i</strong> and <strong>-o</strong> are mandatory arguments. <strong>-f</strong> takes <strong>pdf</strong> as default value.
<ul>
 	<li><strong>Pearson Correlation Matrix:</strong></li>
</ul>
<pre style="text-align: center;"><strong><em>mk_pearson_correlation -i methylKit_Input_Files -o Image_Ouput_File [-f format (pdf, ps, svg, png, jpeg, bmp or tiff)] [-a assembly] [-m methylation_context]</em></strong></pre>
<strong>-i</strong> and <strong>-o</strong> are mandatory arguments. <strong>-f</strong> takes <strong>pdf</strong> as default value. <strong>You should indicate more than one input file, separated by spaces.</strong>
<ul>
 	<li><strong>Clustering Tree:</strong></li>
</ul>
<pre style="text-align: center;"><strong><em>mk_clustering -i methylKit_Input_Files -o Image_Ouput_File [-f format (pdf, ps, svg, png, jpeg, bmp or tiff)] [-a assembly] [-m methylation_context]</em></strong></pre>
<strong>-i</strong> and <strong>-o</strong> are mandatory arguments. <strong>-f</strong> takes <strong>pdf</strong> as default value. <strong>You should indicate more than one input file, separated by spaces.</strong>
<ul>
 	<li><strong>Principal Component Analysis:</strong></li>
</ul>
<pre style="text-align: center;"><strong><em>mk_pca -i methylKit_Input_Files -o Image_Ouput_File [-x a_PC_for_x-axis] [-y another_PC_for_y-axis] [--screenplot] [-f format (pdf, ps, svg, png, jpeg, bmp or tiff)] [-a assembly] [-m methylation_context]</em></strong></pre>
<strong>-i</strong> and <strong>-o</strong> are mandatory arguments. <strong>-f</strong> takes <strong>pdf</strong> as default value. <strong>-x</strong> and <strong>-y</strong> takes <strong>1</strong> and <strong>2</strong> as default values, respectively. <strong>You should indicate more than one input file, separated by spaces.</strong> You can add the optional argument <strong>--screenplot</strong> to get the screenplot. Otherwise you get the PC indicated in x versus PC and indicated.

For further details on the output, see <a href="http://rpubs.com/al2na/methylKit">the manual of methylKit</a>.
<h4><strong>Convert to BED and other formats</strong></h4>
In addition to methylKit intput format, you can convert MethylExtract output files to other formats such as BedGraph, BED6 or bigWig:
<ul>
 	<li><strong>BedGraph, BED6 and BED6+6:</strong></li>
</ul>
<pre style="text-align: center;"><strong><em>me2bed -i MethylExtract_Output_File -o BED_Output_File -f Output_Format (bedgraph, bed6, bed6+6 or ucsc) -c Methylation_Context (CG, CHG or CHH)</em></strong></pre>
<strong>-i</strong>, <strong>-o</strong>, <strong>-f</strong> and <strong>-c</strong> are mandatory arguments.

You can find the specifications of BED and BedGraph formats <a href="https://genome.ucsc.edu/FAQ/FAQformat.html">here</a>.

The <em>score</em> column of the BED file and the <em>dataValue</em> column of the BedGraph file contains a numerical value from 0 to 1000. This value is the methylation level, being 0 completely unmethylated and 1000 completely methylated. The six additional columns of the BED6+6 are:
<ul>
 	<li><strong>Watson METH:</strong> number of reads methylated for this cytosine (referred to the Watson strand).</li>
 	<li><strong>Watson COVERAGE:</strong> reads covering the cytosine in this sequence context (referred to the Watson strand).</li>
 	<li><strong>Watson QUAL:</strong> PHRED score average for the reads covering the cytosine (referred to the Watson strand).</li>
 	<li><strong>Crick METH:</strong> number of reads methylated for this cytosine (referred to the Crick strand).</li>
 	<li><strong>Crick COVERAGE:</strong> reads covering the cytosine in this context (referred to the Crick strand).</li>
 	<li><strong>Crick QUAL:</strong> PHRED score average for the reads covering the cytosine (referred to the Crick strand).</li>
</ul>
For more details of these values visit <a href="http://bioinfo2.ugr.es/MethylExtract/downloads/ManualMethylExtract.pdf">the manual of MethylExtract</a>.
<ul>
 	<li><strong>bigBed:</strong></li>
</ul>
First of all, convert your file to BED6 format. Then get the chromosome sizes file from the assembly multi-FASTA file:
<pre style="text-align: center;"><strong><em>faidx multi-FASTA_input_file -i chromsizes &gt; chrom.sizes</em></strong></pre>
Finally, convert the BED6 input format to bigBed:
<pre style="text-align: center;"><strong><em>bedToBigBed -type=bed6 bed6_input_file chrom.sizes bigBed_output_file</em></strong></pre>
You can find the specifications of bigBed format <a href="https://genome.ucsc.edu/FAQ/FAQformat.html">here</a>.
<ul>
 	<li><strong>bigWig:</strong></li>
</ul>
First of all, convert your file to BedGraph format. Then get the chromosome sizes file from the assembly multi-FASTA file:
<pre style="text-align: center;"><strong><em>faidx multi-FASTA_input_file -i chromsizes &gt; chrom.sizes</em></strong></pre>
Finally, convert the BED6 input format to bigWig:
<pre style="text-align: center;"><strong><em>bedGraphToBigWig bedGraph_input_file chrom.sizes bigWig_output_file</em></strong></pre>
You can find the specifications of bigWig format <a href="https://genome.ucsc.edu/FAQ/FAQformat.html">here</a>.
<h4><strong>Send to a Galaxy Server</strong></h4>
Galaxy gives us the opportunity to do a myriad of analysis. An easy way to send your data to Galaxy from inside virtual machine is using the helper tool <strong><em>upload2galaxy</em></strong>.

To use this tool, first of all you need to get your API key from the Galaxy Server you want to use. To get your <strong>API key</strong>, open a web browser, go to the URL of the Galaxy Server you want to use and login. In the top menu, go to
<pre style="text-align: center;"><strong><em>User </em></strong><strong><em>➜</em></strong><strong><em> Preferences </em></strong><strong><em>➜</em></strong><strong><em> Manage your API keys</em></strong></pre>
Now click on the button Generate a new key now and copy the Current API key. You will use this key to send files to your Galaxy account.

To send a file to your Galaxy account, type:
<pre style="text-align: center;"><strong><em>upload2galaxy [-u URL_of_a_Galaxy_Server] -k API_Key_of_your_Galaxy_Account -i Path_of_the_File_to_Upload [-n Name_of_the_Galaxy_History_to_be_created]</em></strong></pre>
<strong>-i</strong> and <strong>-k</strong> are mandatory arguments. By default <strong>-u</strong> is the URL of the <a href="https://usegalaxy.org/">Galaxy Main Server</a> and <strong>-n</strong> is <em>MethFlow</em>.

To check your uploaded file, in the Galaxy website go to
<pre style="text-align: center;"><strong><em>User </em></strong><strong><em>➜</em></strong><strong><em> Saved Histories</em></strong></pre>
And click on MethFlow or the name indicated with <strong>-n</strong>.
<h4><strong>Upload to UCSC Genome Browser</strong></h4>
One of the best ways to visualize your data is by UCSC Genome Browser. There you can view your data along chromosomes and compare with a myriad of other genomic annotations.

By following these instructions, you can upload your files to UCSC Genome Browser:
<ul>
 	<li>Convert your data to UCSC BED6 format by typing:</li>
</ul>
<pre style="text-align: center;"><strong><em>me2bed -i MethylExtract_Output_File -o BED_Output_File -f ucsc -c Methylation_Context (CG, CHG or CHH)</em></strong></pre>
<strong><em>Note that -f ucsc is required for you to visualize your data correctly.</em></strong>
<ul>
 	<li>Open a browser and go to the UCSC Genome Browser <a href="https://genome.ucsc.edu/">website</a></li>
 	<li>Go to <strong><em>My Data </em></strong><strong><em>➜</em></strong><strong><em> My Sessions</em></strong> in the top menu and login or create an account (your data will continue online after logout).</li>
 	<li>Once logged, go to <strong><em>My Data </em></strong><strong><em>➜</em></strong><strong><em> Custom Tracks</em></strong> in the top menu.</li>
 	<li>Select a file from your local disk and submit it.</li>
 	<li>Once uploaded, select <strong><em>view in Genome Browser</em></strong> and click on <strong><em>go</em></strong>.</li>
</ul>
Now you can browse your data. If you want to upload more files:
<ul>
 	<li>Go to <strong><em>My Data </em></strong><strong><em>➜</em></strong><strong><em> Custom Tracks</em></strong> in the top menu.</li>
 	<li>Click on <strong><em>add custom tracks</em></strong>.</li>
 	<li>Select a file from your local disk and submit it.</li>
 	<li>Once uploaded, select <strong><em>view in Genome Browser</em></strong> and click on <strong><em>go</em></strong>.</li>
</ul>
<h3>External program manuals and documentation</h3>
<ul>
 	<li><strong>fastq-dump (SRA Toolkit):</strong> we use this program to convert files in SRA format to FASTQ format. <a href="http://www.ncbi.nlm.nih.gov/Traces/sra/sra.cgi?view=toolkit_doc&amp;f=fastq-dump">Documentation</a>.</li>
 	<li><strong>Trimmomatic:</strong> we use this program to remove the adapter and low quality bases at the 3’ end. <a href="http://www.usadellab.org/cms/uploads/supplementary/Trimmomatic/TrimmomaticManual_V0.32.pdf">Manual</a>.</li>
 	<li><strong>Bismark:</strong> we use this program to align reads against three-letter reference assemblies. <a href="http://www.bioinformatics.babraham.ac.uk/projects/bismark/Bismark_User_Guide_v0.15.0.pdf">Manual</a>.</li>
 	<li><strong>Bowtie2:</strong> it is the aligner that we use in Bismark. <a href="http://bowtie-bio.sourceforge.net/bowtie2/manual.shtml">Manual</a>.</li>
 	<li><strong>BSeQC:</strong> we use this program to fix the bisulfite bias due to technical factors. <a href="https://github.com/hutuqiu/bseqc/blob/master/README.txt">Documentation</a>.</li>
 	<li><strong>MethylExtract:</strong> the core of MethFlow. We use this program to profile methylations levels and single nucleotide variants. <a href="http://bioinfo2.ugr.es/MethylExtract/downloads/ManualMethylExtract.pdf">Manual</a>.</li>
 	<li><strong>FastQC:</strong> the program that we use to check the quality of FASTQ and trimmed FASTQ files. <a href="http://www.bioinformatics.babraham.ac.uk/projects/fastqc/">Documentation</a>.</li>
 	<li><strong>methylKit: </strong>one of the programs used in differential methylation analysis and the main program used in downstream analysis. <a href="http://rpubs.com/al2na/methylKit">Manual</a>.</li>
 	<li><strong>MOABS:</strong> one of the programs used in differential methylation analysis. <a href="http://dldcc-web.brc.bcm.edu/lilab/deqiangs/moabs/moabs-v1.2.2.pdf">Documentation</a>.</li>
</ul>
