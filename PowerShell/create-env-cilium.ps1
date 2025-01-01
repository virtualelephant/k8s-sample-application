$vcServer = "vcenter-vcf01.home.virtualelephant.com"
$vcUsername = "administrator@vsphere.local"
$vcPassword = "PASSWORD"

Connect-VIServer -Server $vcServer -User $vcUsername -Password $vcPassword
# Variables
$templateName = "cilium-k8s-template"
$destinationFolder = "Cilium"
$datastore = "Synology"  # Replace with your datastore
$cluster = "ve-m01-cluster-001"      # Replace with your cluster

$template = Get-VM -Name $templateName -ErrorAction Stop
$cluster = Get-Cluster -Name $clusterName -ErrorAction Stop
Write-Host "VM Template: $template"
Write-Host "Cluster: $cluster"


# Clone the template multiple times
1..3 | ForEach-Object {
    $vmName = "cilium-c1-cntrl-$($_)" # Define VM name dynamically
    New-VM -Name $vmName -VM $template -Datastore $datastore -Location $destinationFolder -ResourcePool $cluster
    Write-Host "Cloned VM: $vmName"
}

1..5 | ForEach-Object {
    $vmName = "cilium-c1-node-$($_)" # Define VM name dynamically
    New-VM -Name $vmName -VM $template -Datastore $datastore -Location $destinationFolder -ResourcePool $cluster
    Write-Host "Cloned VM: $vmName"
}

# Create HAProxy Load Balancer
$vmName = "cilium-c1-haproxy-1"
New-VM -Name $vmName -VM $template -Datastore $datastore -Location $destinationFolder -ResourcePool $cluster
Write-Host "Cloned VM: $vmName"

# Disconnect from vCenter
Disconnect-VIServer -Server $vcServer -Confirm:$false