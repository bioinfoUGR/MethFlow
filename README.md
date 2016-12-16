# MethFlow
MethFlow is an optimized, open-source pipeline which performs DNA methylation profiling, detection of sequence variants, full integration with our methylation database, _NGSmethDB_, and differential methylation analysis. Briefly, the pipeline performs the following steps:

1.  Format conversion: convert SRA files to FASTQ by means of _SRA Toolkit_. This only applies if the input data comes from Sequence Read Archive (SRA) public repository.
2.  Adapter and low quality bases trimming by means of _Trimmomatic_.
3.  Alignment against one or two assemblies: firstly, short reads are aligned against the first assembly (assembly 1 from now on) producing uniquely-mapped, multiple-mapped and unmapped reads. Uniquely-mapped reads are kept to use in the next step. Secondly, multiple-mapped and/or unmapped reads are aligned against the second assembly (assembly 2 from now on) producing uniquely-mapped, multiple-mapped and unmapped reads. Uniquely-mapped reads are merged with previously obtained uniquely-mapped reads and used in the next step. _Bismark_ is used as aligner.
4.  Elimination of known technical artifacts by _BSeQC_.
5.  Detection of DNA methylation and sequence variants by _MethylExtract_.
6.  Get methylation maps from NGSmethDB.
7.  Differential methylation analysis by _methylKit_ and _MOABS_ and generate a consensus of both.

_MethFlow_ pipeline was inplemented in three ways. We first provide the software optimized to run in a powerful and user-friendly cloud environment. Second, for users requiring the maximal level of data privacy, we developed _MethFlow<sup>VM</sup>_, a ready-to-use, fully-configured virtual machine which is able to run on most operating systems (Windows, Linux or Mac). With _MethFlow<sup>VM</sup>_ the user will no longer need to upload private data to any public server. Finally, advanced users can download the source code from a public repository, which allows installing and customizing _MethFlow_ on any operating system.

## Use in the cloud
Connect to [PrecisionFDA](https://precision.fda.gov/).

## Get MethFlow<sup>VM</sup>
1.  Install [VirtualBox](https://www.virtualbox.org/wiki/Downloads).
2.  Install [VirtualBox Extension Pack](https://www.virtualbox.org/wiki/Downloads).
3.  Download [MethFlow<sup>VM</sup>](http://bioinfo2.ugr.es:8080/MethFlow/download) ([mirror](https://docs.google.com/uc?id=0B6zaHLTx5o2bUWhPOXN0X1F4aEU&export=download)).
4.  Import MethFlow<sup>VM</sup> to VirtualBox by double-clicking.
5.  Optional: [add a shared folder](https://www.virtualbox.org/manual/ch04.html#sharedfolders) (strongly recommended).
6.  Run MethFlow<sup>VM</sup>.

## Install MethFlow (standalone)
### Dependencies
* Python 3 or higher
* Perl 5 or higher
* Java 8 or higher
* [FastQC](http://www.bioinformatics.babraham.ac.uk/projects/fastqc)
* [SRA Toolkit](https://trace.ncbi.nlm.nih.gov/Traces/sra/sra.cgi?view=software) (fastq-dump)
* [Trimmomatic](http://www.usadellab.org/cms/?page=trimmomatic)
* [SAMtools](http://samtools.sourceforge.net) and [pysam](http://pysam.readthedocs.io)
* [Bowtie2](http://bowtie-bio.sourceforge.net/bowtie2) and [Biskmark](http://www.bioinformatics.babraham.ac.uk/projects/bismark)
* [BSeQC](https://github.com/hutuqiu/bseqc)
* [MethylExtract](http://bioinfo2.ugr.es/MethylExtract)
* [methylKit](https://github.com/al2na/methylKit) and [MOABS](https://code.google.com/archive/p/moabs)
* [BioBlend](https://bioblend.readthedocs.io)
* [bedGraphToBigWig](http://hgdownload.soe.ucsc.edu/admin/exe) and [bigWigToBedGraph](http://hgdownload.soe.ucsc.edu/admin/exe)

All these programs must be in the PATH.

### Local Installation
* Execute the following commands:
```bash
git clone https://github.com/bioinfoUGR/MethFlow.git
cd MethFlow
chmod +x MethFlow MethFlow_api MethFlow_diffmeth MethFlow_manager Trimmomatic.sh
```
* In the Trimmomatic.sh file, replace the value of TRIMMOMATIC_PATH by the path of Trimmomatic.jar file.
* Add Trimmomatic.sh to the PATH.

## Quick Start
<span id="ouHighlight__131_134TO132_134">Quick start is thought to try MethFlow without going into details and using the MethFlow virtual machine. For further information, see</span><span id="noHighlight_0.03053827676673926"> </span><span id="ouHighlight__162_163TO158_160">the</span><span id="noHighlight_0.34981369552068187"> [reference manual](http://bioinfo2.ugr.es:8080/MethFlow/reference-manual/)</span><span id="noHighlight_0.8654089653028183">.</span>

### The local database

#### Set your working folder

At first startup, you will be asked which working folder you want to use. If you ignore this question, your home folder, _/home/methflow_, will be used as working folder. If you want to change the working folder, open a terminal and type the following command:

<pre style="text-align: center;">MethFlow_manager working_folder</pre>

#### Set your assembly collection

Tell MethFlow where the assembly collection is by typing:

<pre style="text-align: center;">MethFlow_manager assembly_collection Assemblies</pre>

This command looks for a folder named _Assemblies_ inside the working folder.

#### Set your adapter collection

Tell MethFlow where the adapter collection is by typing:

<pre style="text-align: center;">MethFlow_manager adapter_collection Adapters</pre>

This command looks for a folder named _Adapters_ inside the working folder.

#### Set your root input folder

Tell MethFlow where to look for the input folders:

<pre style="text-align: center;">MethFlow_manager root_input_folder Inputs</pre>

This command looks for a folder named _Inputs_ inside the working folder.

#### Set your root output folder

Tell MethFlow where to kept the output folders:

<pre style="text-align: center;">MethFlow_manager root_output_folder Outputs</pre>

This command creates a folder named _Outputs_ inside the working folder.

#### Get test datasets

Open a terminal and type the following command to get test datasets:

<pre style="text-align: center;">MethFlow_manager get_test_datasets</pre>

Test datasets are then downloaded and unpacked. These test datasets contain:

*   The collection of adapters of [_Trimmomatic_](http://www.usadellab.org/cms/?page=trimmomatic). It goes to adapter collection.
*   A small assembly (chromosomes 12 and 19 of hg38). It goes to assemby collection.
*   Data from nine samples (from three individuals and three tissues). It goes to root input folder.

### Launch MethFlow

Now, launch MethFlow with default options:

<pre style="text-align: center;">MethFlow</pre>

This command looks inside the working folder and asks you for:

1.  **Assembly 1 folder.** This folder should contain FASTA or multiFASTA files and must be inside assembly collection folder. Optionally, it could contain Bismark Bowtie2 indexes.
2.  **Adapter file.** This file must be a multiFASTA file inside adapter collection.
3.  **Input data folder(s).** Each of these folders should contain all the input datasets of a sample in SRA, FASTQ, SAM or BAM format (all files must be in the same format) and must be inside the root input folder.

If you want to use a second assembly, launch MethFlow as follow:

<pre style="text-align: center;">MethFlow ‐‐assembly2</pre>

In this case, MethFlow asks you for:

1.  **Assembly 1 folder.** This folder should contain FASTA or multiFASTA files and must be inside assembly collection folder. Optionally, it could contain Bismark Bowtie2 indexes.
2.  **Assembly 2 folder.** This folder should contain FASTA or multiFASTA files and must be inside assembly collection folder. Optionally, it could contain Bismark Bowtie2 indexes.
3.  **What type of reads you want to use against the assembly 2:** multiple-mapped reads, unmapped reads or both.
4.  **Adapter file.** This file must be a multiFASTA file inside adapter collection.
5.  **Input data folder(s).** Each of these folders should contain all the input datasets of a sample in SRA, FASTQ, SAM or BAM format (all files must be in the same format) and must be inside the root input folder.

<span id="ouHighlight__0_13TO0_11" class="">Additionally</span><span id="noHighlight_0.8676234614908152">,</span> <span id="noHighlight_0.6976494981161827"></span> <span id="ouHighlight__16_18TO14_16" class="">use</span> <span id="noHighlight_0.0906570260582924"></span> <span id="ouHighlight__20_22TO18_20">the</span> <span id="noHighlight_0.5782996075823763"></span> <span id="ouHighlight__24_31TO22_28">options</span><span id="noHighlight_0.14885440070328393"> **‐‐enable_api**</span><span id="noHighlight_0.11344022272910004"> </span><span id="ouHighlight__36_36TO34_36">and</span> <span id="noHighlight_0.8178921835612691">**‐‐enable_diffmeth**</span><span id="noHighlight_0.5483406972786837"> </span><span id="ouHighlight__41_44TO42_43">to</span> <span id="noHighlight_0.7456307411930678"></span> <span id="ouHighlight__46_52TO45_52">activate</span><span id="noHighlight_0.6097980775447114"> NGSmethDB API client</span><span id="noHighlight_0.19534596049887143"> </span><span id="ouHighlight__56_56TO56_58">and</span><span id="noHighlight_0.3839531351818044"> differential methylation analysis functionalities</span><span id="ouHighlight__58_59TO60_61">,</span> <span id="noHighlight_0.714314756293355"></span> <span id="ouHighlight__61_75TO63_74">respectively</span><span id="noHighlight_0.6297298994401557">.</span> <span id="noHighlight_0.5849362428588822"></span> <span id="ouHighlight__78_85TO77_84">MethFlow asks </span><span id="noHighlight_0.8807107168266013"></span><span id="ouHighlight__87_88TO86_88">you</span> <span id="noHighlight_0.9520375869905775"></span> <span id="ouHighlight__101_103TO97_100">what</span> <span id="noHighlight_0.4112756769424726"></span> <span id="ouHighlight__105_112TO102_108" class="">samples</span><span id="noHighlight_0.9787954657415041"> you want to </span><span id="ouHighlight__114_122TO110_117" class="">download</span><span id="noHighlight_0.5888984200260194"> from</span><span id="noHighlight_0.2157172174708979"> </span><span id="ouHighlight__127_128TO122_124">the</span> <span id="noHighlight_0.33090849979118264"></span> <span id="ouHighlight__130_138TO126_134">NGSmethDB</span> <span id="noHighlight_0.7411572490619205"></span> <span id="ouHighlight__140_140TO136_138">and</span><span id="noHighlight_0.14002499373866995"> what</span><span id="noHighlight_0.5886416442989675"> </span><span id="ouHighlight__146_153TO145_151">samples</span> <span id="noHighlight_0.9673121861636826"></span> <span id="ouHighlight__155_162TO153_159">compare </span><span id="noHighlight_0.4510468058318138"></span><span id="ouHighlight__164_165TO161_162">in</span> <span id="noHighlight_0.9755744369350245"></span> <span id="ouHighlight__167_168TO164_166" class="">the </span><span id="ouHighlight__193_203TO192_203" class="">differential<span id="noHighlight_0.2595808121142329"> </span><span id="ouHighlight__182_191TO180_190" class="">methylation</span> <span id="noHighlight_0.7804256309098638"></span> analysis</span><span id="noHighlight_0.9979496553751572">.</span>

### A look at the output

*   **Intermediates folder:** <span id="ouHighlight__14_18TO14_16" class="">all</span> <span id="noHighlight_0.07545820414138715"></span> <span id="ouHighlight__20_22TO18_20">the</span> <span id="noHighlight_0.9153987486654813"></span> <span id="ouHighlight__33_43TO28_39">intermediate files</span> <span id="noHighlight_0.1286313150550824"></span> <span id="ouHighlight__45_53TO41_49" class="">generated</span> <span id="noHighlight_0.9301825002908815"></span> <span id="ouHighlight__55_61TO51_56" class="">during</span> <span id="noHighlight_0.08993821523127776"></span> <span id="ouHighlight__63_64TO58_60" class="">the</span> <span id="noHighlight_0.6872673620335985"></span> <span id="ouHighlight__66_73TO62_69" class="">analysis</span><span id="noHighlight_0.22142384692696315">.</span>It <span id="ouHighlight__5_12TO5_12" class="">contains a folder for each analyzed sample.</span>
*   **Plots folder:**<span id="noHighlight_0.7301467444298817"> </span><span id="ouHighlight__18_22TO16_20" class="">plots</span> <span id="noHighlight_0.5475378065103533"></span> <span id="ouHighlight__24_32TO22_30" class="">generated</span> <span id="noHighlight_0.02068600755891703"></span> <span id="ouHighlight__34_36TO32_33" class="">by</span> <span id="noHighlight_0.9507322942728866"></span> <span id="ouHighlight__38_43TO35_40" class="">FastQC</span><span id="noHighlight_0.413405703844135">,</span> <span id="noHighlight_0.6919898626085998"></span> <span id="ouHighlight__46_50TO43_47" class="">BSeQC</span> <span id="noHighlight_0.06013854719396283"></span> <span id="ouHighlight__52_52TO49_51" class="">and</span> <span id="noHighlight_0.21523532471035267"></span> <span id="ouHighlight__54_62TO53_61" class="">methylKit</span><span id="noHighlight_0.9295557173953668">.It <span id="ouHighlight__5_12TO5_12" class="">contains a folder for each analyzed sample.</span></span>
*   **Meth folder:**<span id="noHighlight_0.5578221021297478"> all </span><span id="ouHighlight__27_36TO16_26" class="">methylation</span> <span id="noHighlight_0.4938989405898653"></span> <span id="ouHighlight__18_22TO28_31" class="">maps</span> <span id="noHighlight_0.38932746822653286"></span> <span id="ouHighlight__38_47TO33_42" class="">calculated</span><span id="noHighlight_0.3796660264738987"> </span><span id="ouHighlight__49_51TO44_45">by</span> <span id="noHighlight_0.39273337788664775"></span> <span id="ouHighlight__53_60TO47_54" class="">MethFlow</span><span id="noHighlight_0.8177048184320586">.</span> <span id="noHighlight_0.616119880618601">It <span id="ouHighlight__5_12TO5_12" class="">contains a folder for each analyzed sample.</span></span>

If you use the NGSmethDB API client functionality, each of the downloaded methylation maps will be stored in a folder inside the Meth folder. If you use the differential methylation analysis functionality, you will have an additional output folder:

*   **Diffmeth folder:** all<span id="noHighlight_0.8250479858252433"> </span><span id="ouHighlight__38_48TO16_27" class="">differential</span> <span id="noHighlight_0.45999008923868123"></span> <span id="ouHighlight__27_36TO29_39" class="">methylation</span> <span id="noHighlight_0.5553820625838168"></span> <span id="ouHighlight__18_22TO41_44">maps</span> <span id="noHighlight_0.19512951934003575"></span> <span id="ouHighlight__50_59TO46_55">calculated</span> <span id="noHighlight_0.28837372236284753"></span> <span id="ouHighlight__61_63TO57_58">by</span> <span id="noHighlight_0.24902246054852317"></span> <span id="ouHighlight__65_72TO60_67">MethFlow<span id="noHighlight_0.8177048184320586">.</span> <span id="noHighlight_0.616119880618601">It <span id="ouHighlight__5_12TO5_12" class="">contains a folder for each pair of samples used in the differential methylation analysis.</span></span></span>
