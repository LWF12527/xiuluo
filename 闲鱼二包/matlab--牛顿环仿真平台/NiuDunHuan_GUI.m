function varargout = NiuDunHuan_GUI(varargin)
% NIUDUNHUAN_GUI MATLAB code for NiuDunHuan_GUI.fig
%      NIUDUNHUAN_GUI, by itself, creates a new NIUDUNHUAN_GUI or raises the existing
%      singleton*.
%
%      H = NIUDUNHUAN_GUI returns the handle to a new NIUDUNHUAN_GUI or the handle to
%      the existing singleton*.
%
%      NIUDUNHUAN_GUI('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in NIUDUNHUAN_GUI.M with the given input arguments.
%
%      NIUDUNHUAN_GUI('Property','Value',...) creates a new NIUDUNHUAN_GUI or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before NiuDunHuan_GUI_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to NiuDunHuan_GUI_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help NiuDunHuan_GUI

% Last Modified by GUIDE v2.5 27-Sep-2020 00:46:15

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @NiuDunHuan_GUI_OpeningFcn, ...
                   'gui_OutputFcn',  @NiuDunHuan_GUI_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT


% --- Executes just before NiuDunHuan_GUI is made visible.
function NiuDunHuan_GUI_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to NiuDunHuan_GUI (see VARARGIN)

% Choose default command line output for NiuDunHuan_GUI
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes NiuDunHuan_GUI wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = NiuDunHuan_GUI_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;



function edit_bc_Callback(hObject, eventdata, handles)
% hObject    handle to edit_bc (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit_bc as text
%        str2double(get(hObject,'String')) returns contents of edit_bc as a double


% --- Executes during object creation, after setting all properties.
function edit_bc_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_bc (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function edit_bj_Callback(hObject, eventdata, handles)
% hObject    handle to edit_bj (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit_bj as text
%        str2double(get(hObject,'String')) returns contents of edit_bj as a double


% --- Executes during object creation, after setting all properties.
function edit_bj_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_bj (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in pushbutton1.
function pushbutton1_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global flag ;
global t;
global X;
global Y;
global Lambda;
global R;
rm = 2;                                 %正方形画面边长的一半（mm）
temp = linspace(-rm, rm, 301);
[X, Y] = meshgrid(temp);                %创建用于绘制二维图像的矩阵
R = eval(handles.edit_bj.String);             %平凸透镜的半径（mm）
Lambda = eval(handles.edit_bc.String)*1e-6;     %入射光波长（mm）
t = 0;
flag = 1;
d = (X.^2 + Y.^2)./(2 * R);     %计算空气薄膜厚度
Delte = d/Lambda * 2*pi + pi;
I = 128*(cos(Delte/2)).^2;            %计算相对光强
image(handles.axes1,I);
colormap gray
axis off
axis equal
title('牛顿环(Newton ring)','FontSize',12);



% --- Executes on button press in pushbutton5.
function pushbutton5_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global flag;
flag = 0;
cla(handles.axes1);


% --- Executes on button press in pushbutton6.
function pushbutton6_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton6 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global flag ;
global t;
global X;
global Y;
global Lambda;
global R;
if(flag ~= 0)
    flag = 2;
end
while flag == 2
    d = (X.^2 + Y.^2)./(2 * R) + t;     %计算空气薄膜厚度
    Delte = d/Lambda * 2*pi + pi;
    I = 128*(cos(Delte/2)).^2;            %计算相对光强
    image(handles.axes1,I);
    title('牛顿环(Newton ring)','FontSize',12);
    colormap gray
    axis off
    axis equal
    pause(0.2);
    t = t+0.00003;
end

% --- Executes on button press in pushbutton7.
function pushbutton7_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton7 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global flag ;
global t;
global X;
global Y;
global Lambda;
global R;
if(flag ~= 0)
    flag = 2;
end
while flag == 2
    d = (X.^2 + Y.^2)./(2 * R) + t;     %计算空气薄膜厚度
    Delte = d/Lambda * 2*pi + pi;
    I = 128*(cos(Delte/2)).^2;            %计算相对光强
    image(handles.axes1,I);
    title('牛顿环(Newton ring)','FontSize',12);
    colormap gray
    axis off
    axis equal
    pause(0.2);
    t = t-0.00003;
end


% --- Executes on button press in pushbutton8.
function pushbutton8_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton8 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global flag
title('牛顿环(Newton ring)','FontSize',12);
flag = 0;
pause(0.5);
flag = 1;


% --- Executes on button press in pushbutton9.
function pushbutton9_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton9 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global flag ;
global t;
global X;
global Y;
global Lambda;
global R;
rm = 2;                                 %正方形画面边长的一半（mm）
temp = linspace(-rm, rm, 301);
[X, Y] = meshgrid(temp);                %创建用于绘制二维图像的矩阵
R = eval(handles.edit_bj.String);             %平凸透镜的半径（mm）
Lambda = eval(handles.edit_bc.String)*1e-6;     %入射光波长（mm）
t = 0;
flag = 1;
d = (X.^2 + Y.^2)./(2 * R);     %计算空气薄膜厚度
Delte = d/Lambda * 2*pi + pi;
I = 128*(cos(Delte/2)).^2;            %计算相对光强
image(handles.axes1,I);
colormap gray
axis off
axis equal
title('牛顿环(Newton ring)','FontSize',12);
